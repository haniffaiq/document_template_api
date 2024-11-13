from flask import jsonify, request
from db import db
from sqlalchemy.sql import text
from datetime import datetime
from decimal import Decimal
# Fungsi untuk membuat produk baru menggunakan query mentah dengan text()
def create_product(data):
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock_quantity = data.get('stock_quantity', 0)

    # Query untuk mengecek apakah produk sudah ada
    check_query = text("""
    SELECT 1 FROM core.products WHERE name = :name AND is_deleted = 0
    """)
    existing_product = db.session.execute(check_query, {'name': name}).fetchone()

    if existing_product:
        return jsonify({"status": 400, "message": "Product already exists"}), 400

    # Query untuk menambahkan produk baru
    insert_query = text("""
    INSERT INTO core.products (id, name, description, price, stock_quantity, created_at, updated_at)
    VALUES (gen_random_uuid(), :name, :description, :price, :stock_quantity, NOW(), NOW())
    """)
    db.session.execute(insert_query, {
        'name': name,
        'description': description,
        'price': price,
        'stock_quantity': stock_quantity
    })
    db.session.commit()

    return jsonify({"status": 201, "message": "Product created successfully"}), 201


# Fungsi untuk mengambil semua produk menggunakan query mentah dengan text()
def get_products():
    query = text("""
    SELECT id, name, description, price, stock_quantity, created_at, updated_at 
    FROM core.products WHERE is_deleted = 0
    """)
    result = db.session.execute(query).fetchall()

    products = [{
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'price': str(row[3]),
        'stock_quantity': row[4],
        'created_at': row[5],
        'updated_at': row[6]
    } for row in result]

    return jsonify(products), 200


# Fungsi untuk mengambil produk berdasarkan ID menggunakan query mentah dengan text()
def get_product_by_id(product_id):
    query = text("""
    SELECT id, name, description, price, stock_quantity, created_at, updated_at
    FROM core.products WHERE id = :product_id AND is_deleted = 0
    """)
    result = db.session.execute(query, {'product_id': product_id}).fetchone()

    if not result:
        return jsonify({"status": 404, "message": "Product not found"}), 404

    product = {
        'id': result[0],
        'name': result[1],
        'description': result[2],
        'price': str(result[3]),
        'stock_quantity': result[4],
        'created_at': result[5],
        'updated_at': result[6]
    }
    return jsonify(product), 200


# Fungsi untuk memperbarui produk menggunakan query mentah dengan text()
def update_product(product_id, data):
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock_quantity = data.get('stock_quantity')

    # Query untuk memperbarui produk
    update_query = text("""
    UPDATE core.products
    SET name = :name, description = :description, price = :price, stock_quantity = :stock_quantity,
        updated_at = NOW()
    WHERE id = :product_id AND is_deleted = 0
    """)
    result = db.session.execute(update_query, {
        'name': name,
        'description': description,
        'price': price,
        'stock_quantity': stock_quantity,
        'product_id': product_id
    })
    db.session.commit()

    if result.rowcount == 0:
        return jsonify({"status": 404, "message": "Product not found"}), 404

    return jsonify({"status": 200, "message": "Product updated successfully"}), 200


# Fungsi untuk menghapus produk secara logis menggunakan query mentah dengan text()
def delete_product(product_id):
    # Query untuk menghapus produk
    delete_query = text("""
    UPDATE core.products
    SET is_deleted = 1, deleted_at = NOW()
    WHERE id = :product_id AND is_deleted = 0
    """)
    result = db.session.execute(delete_query, {'product_id': product_id})
    db.session.commit()

    if result.rowcount == 0:
        return jsonify({"status": 404, "message": "Product not found"}), 404

    return jsonify({"status": 200, "message": "Product deleted successfully"}), 200



def create_stock_movement(data):
    product_id = data.get('product_id')
    movement_type = data.get('movement_type')
    quantity = data.get('quantity')
    unit_price = data.get('unit_price')
    description = data.get('description')

    # Cek apakah produk ada
    product_check_query = text("""
    SELECT id, stock_quantity FROM core.products WHERE id = :product_id AND is_deleted = 0
    """)
    product = db.session.execute(product_check_query, {'product_id': product_id}).fetchone()

    if not product:
        return jsonify({"status": 404, "message": "Product not found"}), 404

    # Ambil jumlah stok yang ada
    available_stock = product[1]

    # Validasi jika pergerakan barang keluar melebihi stok yang ada
    if movement_type == 'out' and quantity > available_stock:
        return jsonify({
            "status": 400,
            "message": f"Insufficient stock: Available stock is {available_stock}, but trying to move out {quantity}."
        }), 400

    # Menyimpan pergerakan stok
    insert_movement_query = text("""
    INSERT INTO core.stock_movements (id, product_id, movement_type, quantity, unit_price, movement_date, description, created_at, updated_at)
    VALUES (gen_random_uuid(), :product_id, :movement_type, :quantity, :unit_price, NOW(), :description, NOW(), NOW())
    """)
    db.session.execute(insert_movement_query, {
        'product_id': product_id,
        'movement_type': movement_type,
        'quantity': quantity,
        'unit_price': unit_price,
        'description': description
    })
    db.session.commit()

    # Update stock_quantity produk setelah pergerakan stok
    if movement_type == 'in':
        update_stock_query = text("""
        UPDATE core.products
        SET stock_quantity = stock_quantity + :quantity
        WHERE id = :product_id AND is_deleted = 0
        """)
    elif movement_type == 'out':
        update_stock_query = text("""
        UPDATE core.products
        SET stock_quantity = stock_quantity - :quantity
        WHERE id = :product_id AND is_deleted = 0
        """)

    db.session.execute(update_stock_query, {'product_id': product_id, 'quantity': quantity})
    db.session.commit()

    return jsonify({"status": 201, "message": "Stock movement recorded successfully"}), 201


def monitor_stock():
    # Query untuk mendapatkan data stok dan total revenue
    query = text("""
    SELECT 
        p.id, 
        p.name, 
        p.stock_quantity,  -- Stok awal dari produk
        p.price, 
        SUM(CASE WHEN sm.movement_type = 'in' THEN sm.quantity ELSE 0 END) AS total_in_stock,  -- Stok masuk
        SUM(CASE WHEN sm.movement_type = 'out' THEN sm.quantity ELSE 0 END) AS total_out_stock  -- Stok keluar
    FROM core.products p
    LEFT JOIN core.stock_movements sm 
        ON p.id = sm.product_id
    WHERE p.is_deleted = 0  -- Hanya produk yang belum dihapus
    GROUP BY p.id
    """)

    # Menjalankan query dan mendapatkan hasil
    result = db.session.execute(query).fetchall()

    stock_data = []
    total_revenue = Decimal(0.0)  # Menggunakan Decimal untuk total revenue

    for row in result:
        product_id = row[0]
        product_name = row[1]
        initial_stock = row[2]  # Stok awal dari produk
        price = Decimal(row[3])  # Mengonversi price menjadi Decimal untuk konsistensi
        total_in_stock = row[4]  # Total stok masuk
        total_out_stock = row[5]  # Total stok keluar

        # Menghitung stok saat ini
        current_stock = initial_stock

        # Menghitung revenue (berdasarkan barang keluar)
        revenue = total_out_stock * price

        # Menambahkan data produk ke dalam list
        stock_data.append({
            'product_id': product_id,
            'product_name': product_name,
            'current_stock': current_stock,
            'total_in_stock': total_in_stock,
            'total_out_stock': total_out_stock,
            'price': str(price),  # Konversi Decimal menjadi string untuk JSON
        })

        # Menambahkan revenue ke total_revenue
        total_revenue += revenue

    # Mengembalikan response dengan data stok dan total revenue
    return jsonify({"stock_data": stock_data, "total_revenue": str(total_revenue)}), 200
