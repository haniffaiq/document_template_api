from flask import Blueprint, request
from controllers.core.dynamic_controller import *

crud_bp = Blueprint('crud', __name__)

# POST: Create a new record in the specified table
@crud_bp.route('/crud/post/<table_name>', methods=['POST'])
def create(table_name):
    data = request.get_json()
    return create_record(table_name, data)

# GET: Retrieve records (either all or by ID)
@crud_bp.route('/crud/get/<table_name>', methods=['GET'])
def get(table_name):
    record_id = request.args.get('id', None)
    return get_records(table_name, record_id)

# PUT: Update an existing record by ID
@crud_bp.route('/crud/put/<table_name>', methods=['PUT'])
def update(table_name):
    data = request.get_json()
    record_id = request.args.get('id', None)
    if not record_id:
        return jsonify({"error": "ID is required for update"}), 400
    return update_record(table_name, data, record_id)

# DELETE: Delete an existing record by ID
@crud_bp.route('/crud/delete/<table_name>', methods=['DELETE'])
def delete(table_name):
    record_id = request.args.get('id', None)
    if not record_id:
        return jsonify({"error": "ID is required for delete"}), 400
    return delete_record(table_name, record_id)
