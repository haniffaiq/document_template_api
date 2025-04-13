from flask import jsonify, request
from db import db
from models.core.project import Project 
# Helper function to get model based on table name
def get_model_by_name(table_name):
    # if table_name == 'project':
    #     from models.core.project import Project, db
    #     return Project
    if table_name == 'surat_pernyataan':  # Example for another table
        from models.core.surat_pernyataan import SuratPernyataan
        return SuratPernyataan
    elif table_name == 'ringkasan_kontrak':  # Example for another table
        from models.core.ringkasan_kontrak import RingkasanKontrak
        return RingkasanKontrak
    elif table_name == 'berita_acara_pembayaran_termin':  # Example for another table
        from models.core.berita_acara_pembayaran_termin import BeritaAcaraPembayaranTermin
        return BeritaAcaraPembayaranTermin
    elif table_name == 'berita_acara_pembayaran_tahap':  # Example for another table
        from models.core.berita_acara_pembayaran_tahap import BeritaAcaraPembayaranTahap
        return BeritaAcaraPembayaranTahap
    elif table_name == 'kwitansi_tahap':  # Example for another table
        from models.core.kwitansi_tahap import KwitansiTahap
        return KwitansiTahap
    elif table_name == 'kwitansi_termin':  # Example for another table
        from models.core.kwitansi_termin import KwitansiTermin
        return KwitansiTermin
    elif table_name == 'berita_acara_serah_terima_uang_muka':  # Example for another table
        from models.core.berita_acara_serah_terima_uang_muka import BeritaAcaraSerahTerimaUangMuka
        return BeritaAcaraSerahTerimaUangMuka
    elif table_name == 'lampiran_berita_acara_serah_terima_uang_muka':  # Example for another table
        from models.core.lampiran_berita_acara_serah_terima_uang_muka import LampiranBeritaAcaraSerahTerimaUangMuka
        return LampiranBeritaAcaraSerahTerimaUangMuka
    elif table_name == 'berita_acara_pemeriksaan_pekerjaan':  # Example for another table
        from models.core.berita_acara_pemeriksaan_pekerjaan import BeritaAcaraPemeriksaanPekerjaan
        return BeritaAcaraPemeriksaanPekerjaan
    
    elif table_name == 'berita_acara_pemeriksaan_tahap_ke':  # Example for another table
        from models.core.berita_acara_pemeriksaan_tahap_ke import BeritaAcaraPemeriksaanTahapKe
        return BeritaAcaraPemeriksaanTahapKe
    elif table_name == 'lampiran_berita_acara_pemeriksaan_tahap_ke':  # Example for another table
        from models.core.lampiran_berita_acara_pemeriksaan_tahap_ke import LampiranBeritaAcaraPemeriksaanTahapKe
        return LampiranBeritaAcaraPemeriksaanTahapKe
    elif table_name == 'berita_acara_serah_terima_pekerjaan_perencanaan':  # Example for another table
        from models.core.berita_acara_serah_terima_pekerjaan_perencanaan import BeritaAcaraSerahTerimaPekerjaanPerencanaan
        return BeritaAcaraSerahTerimaPekerjaanPerencanaan
    elif table_name == 'lampiran_berita_acara_pemeriksaan_pekerjaan':  # Example for another table
        from models.core.lampiran_berita_acara_pemeriksaan_pekerjaan import LampiranBeritaAcaraPemeriksaanPekerjaan
        return LampiranBeritaAcaraPemeriksaanPekerjaan
    
    elif table_name == 'berita_acara_serah_terima_pekerjaan_pengawasan':  # Example for another table
        from models.core.berita_acara_serah_terima_pekerjaan_pengawasan import BeritaAcaraSerahTerimaPekerjaanPengawasan
        return BeritaAcaraSerahTerimaPekerjaanPengawasan
    elif table_name == 'surat_penunjukan_penyedia_barang_jasa':  # Example for another table
        from models.core.surat_penunjukan_penyedia_barang_jasa import SuratPenunjukanPenyediaBarangJasa
        return SuratPenunjukanPenyediaBarangJasa
    elif table_name == 'surat_perintah_mulai_kerja':  # Example for another table
        from models.core.surat_perintah_mulai_kerja import SuratPerintahMulaiKerja
        return SuratPerintahMulaiKerja
    elif table_name == 'surat_perjanjian_kontrak':  # Example for another table
        from models.core.surat_perjanjian_kontrak import SuratPerjanjianKontrak
        return SuratPerjanjianKontrak
    elif table_name == 'syarat_syarat_khusus_kontrak':  # Example for another table
        from models.core.syarat_syarat_khusus_kontrak import SyaratSyaratKhususKontrak
        return SyaratSyaratKhususKontrak
    
    elif table_name == 'history':  # Example for another table
        from models.core.history import HistoryCrud
        return HistoryCrud
    # Add more tables as necessary...
    else:
        return None

# POST: Create a new record in the specified table
def create_record(table_name, data):
    model = get_model_by_name(table_name)
    
    if not model:
        return jsonify({"error": f"Table {table_name} not found"}), 404
    
    try:
        # Dynamically create a new record
        new_record = model(**data)
        db.session.add(new_record)
        db.session.commit()
        return jsonify(new_record.as_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def get_records_with_project(table_name, record_id=None):
    # Dynamically get the model based on the table_name
    model = get_model_by_name(table_name)
    
    if not model:
        return jsonify({"error": f"Table {table_name} not found"}), 404

    if record_id:
        # Get record by ID with LEFT JOIN on Project
        record = db.session.query(model).outerjoin(Project, model.project_id == Project.id).filter(model.id == record_id).first()

        if not record:
            return jsonify({"error": "Record not found"}), 404

        # Convert the record to a dictionary
        result = record.as_dict()

        # Include project data in the response if the record has a related project
        if record.project:
            result['project'] = record.project.as_dict()

        return jsonify(result), 200
    else:
        # Get all records with LEFT JOIN on Project
        records = db.session.query(model).outerjoin(Project, model.project_id == Project.id).all()

        # Convert records to a list of dictionaries
        result_list = []
        for record in records:
            record_dict = record.as_dict()

            # Include project data in the response if the record has a related project
            if record.project:
                record_dict['project'] = record.project.as_dict()

            result_list.append(record_dict)

        return jsonify(result_list), 200
    
# GET: Retrieve records (either all or by ID)
def get_records(table_name, record_id=None):
    model = get_model_by_name(table_name)
    
    if not model:
        return jsonify({"error": f"Table {table_name} not found"}), 404

    if record_id:
        # Get record by ID
        record = model.query.get(record_id)
        if not record:
            return jsonify({"error": "Record not found"}), 404
        return jsonify(record.as_dict()), 200
    else:
        # Get all records
        records = model.query.all()
        return jsonify([record.as_dict() for record in records]), 200

# def get_records(table_name, record_id=None):
#     # Retrieve model dynamically by table name
#     model = get_model_by_name(table_name)
    
#     if not model:
#         return jsonify({"error": f"Table {table_name} not found"}), 404

#     # Retrieve the project model
#     project_model = get_model_by_name('project')
#     if project_model:
#         # Perform a join based on `project_id` column in the `model` table
#         query = model.query.join(project_model, model.project_id == project_model.id)
#     else:
#         query = model.query  # If no 'project' table, just return the table's records

#     if record_id:
#         # Get a single record by ID and join the 'project' table
#         record = query.get(record_id)
#         if not record:
#             return jsonify({"error": "Record not found"}), 404
        
#         # Combine model and project data
#         result = record.as_dict()
        
#         # Add project fields to the result (assuming 'project' relation exists)
#         project = record.project  # This assumes the relationship is set up properly in the model
#         if project:
#             result['project'] = project.as_dict()
        
#         return jsonify(result), 200
#     else:
#         # Get all records with the join to the 'project' table
#         records = query.all()
        
#         # Use a dictionary to store results grouped by project_id
#         grouped_results = {}

#         # Loop over all records to group them by project_id
#         for record in records:
#             project = record.project  # Assuming the relationship is set up correctly
            
#             if project:
#                 project_data = project.as_dict()
                
#                 # If the project is not yet in the grouped results, initialize it
#                 if project.id not in grouped_results:
#                     grouped_results[project.id] = {
#                         'project': project_data,
#                         'records': []
#                     }
                
#                 # Add the current record to the "records" list for the correct project
#                 record_data = record.as_dict()
#                 grouped_results[project.id]['records'].append(record_data)
        
#         # Convert the grouped results into a list to return
#         final_results = []

#         # Prepare the final structure as an array of project records
#         for project_id, group in grouped_results.items():
#             # Add records inside the "project" object
#             project_info = group['project']
#             project_info['records'] = group['records']
            
#             final_results.append({
#                 'project': project_info  # project with associated records inside
#             })

#         return jsonify(final_results), 200

# PUT: Update an existing record by ID
def update_record(table_name, data, record_id):
    model = get_model_by_name(table_name)
    
    if not model:
        return jsonify({"error": f"Table {table_name} not found"}), 404

    # Get the record to be updated
    record = model.query.get(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404

    try:
        # Update fields dynamically
        for key, value in data.items():
            if hasattr(record, key):
                setattr(record, key, value)
        db.session.commit()
        return jsonify(record.as_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# DELETE: Delete an existing record by ID
def delete_record(table_name, record_id):
    model = get_model_by_name(table_name)
    
    if not model:
        return jsonify({"error": f"Table {table_name} not found"}), 404

    # Get the record to be deleted
    record = model.query.get(record_id)
    if not record:
        return jsonify({"error": "Record not found"}), 404

    try:
        db.session.delete(record)
        db.session.commit()
        return jsonify({"message": "Record deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
