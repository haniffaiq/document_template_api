from flask import request, jsonify
from models.core.project import Project, db
from datetime import datetime
from models.core.project import Project
from models.core.surat_pernyataan import SuratPernyataan
from models.core.ringkasan_kontrak import RingkasanKontrak
from models.core.berita_acara_pembayaran_termin import BeritaAcaraPembayaranTermin
from models.core.berita_acara_pembayaran_tahap import BeritaAcaraPembayaranTahap
from models.core.kwitansi import Kwitansi
from models.core.berita_acara_serah_terima_uang_muka import BeritaAcaraSerahTerimaUangMuka
from models.core.lampiran_berita_acara_serah_terima_uang_muka import LampiranBeritaAcaraSerahTerimaUangMuka

# Create a new project
def create_project(data):
    
    # Ensure date fields are formatted properly
    date_fields = [
        'tanggal_surat_bap', 'tanggal_berita_acara_pemeriksaan_pekerjaan',
        'tanggal_surat_penunjukan_penyedia_barang_jasa_sppbj', 
        'tanggal_surat_perjanjian_kontrak', 'tanggal_nomor_akta_notaris_pihak_2'
    ]
    
    for field in date_fields:
        if field in data:
            try:
                # Try to parse the date field
                data[field] = datetime.strptime(data[field], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({"error": f"Invalid date format for {field}. Expected YYYY-MM-DD."}), 400
    
    # Dynamically create an instance of the Project model
    project = Project(**data)

    try:
        db.session.add(project)
        db.session.commit()
        return jsonify(project.as_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def get_all_projects():
    try:
        # Fetch all projects from the database
        projects = Project.query.all()
        
        # Convert each project to a dictionary format
        project_list = [project.as_dict() for project in projects]
        
        return jsonify(project_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# def get_project_by_id(id):
#     try:
#         # Fetch the project by ID
#         project = Project.query.get(id)
        
#         # If project not found, return 404 error
#         if not project:
#             return jsonify({"error": "Project not found"}), 404
        
#         return jsonify(project.as_dict()), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
def get_tables_with_project_id(id):
    # Get the project_id from request arguments
    project_id = id
    
    if not project_id:
        return jsonify({"error": "Project ID is required"}), 400

    try:
        # List of models to search for project_id
        models = [
            ('surat_pernyataan', SuratPernyataan),
            ('ringkasan_kontrak', RingkasanKontrak),
            ('berita_acara_pembayaran_termin', BeritaAcaraPembayaranTermin),
            ('berita_acara_pembayaran_tahap', BeritaAcaraPembayaranTahap),
            ('kwitansi', Kwitansi),
            ('berita_acara_serah_terima_uang_muka', BeritaAcaraSerahTerimaUangMuka),
            ('lampiran_berita_acara_serah_terima_uang_muka', LampiranBeritaAcaraSerahTerimaUangMuka)
        ]
        
        result = []

        for table_name, model in models:
            records = db.session.query(model.id).filter(model.project_id == project_id).all()

            for record in records:
                result.append({
                    'document_name': table_name,
                    'id': record.id,
                })
        
        # If no records found, return a message
        if not result:
            return jsonify({"message": "No records found with the specified project_id"}), 404

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
def update_project(id, data):
    
    try:
        # Fetch the project by ID
        project = Project.query.get(id)
        
        if not project:
            return jsonify({"error": "Project not found"}), 404
        
        # Update the fields of the project with the provided data
        for key, value in data.items():
            if hasattr(project, key):
                setattr(project, key, value)

        # Ensure date fields are formatted properly
        date_fields = [
            'tanggal_surat_bap', 'tanggal_berita_acara_pemeriksaan_pekerjaan',
            'tanggal_surat_penunjukan_penyedia_barang_jasa_sppbj', 
            'tanggal_surat_perjanjian_kontrak', 'tanggal_nomor_akta_notaris_pihak_2'
        ]
        
        for field in date_fields:
            if field in data:
                try:
                    # Try to parse the date field
                    setattr(project, field, datetime.strptime(data[field], '%Y-%m-%d').date())
                except ValueError:
                    return jsonify({"error": f"Invalid date format for {field}. Expected YYYY-MM-DD."}), 400
        
        db.session.commit()
        return jsonify(project.as_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def delete_project(id):
    try:
        # Fetch the project by ID
        project = Project.query.get(id)
        
        if not project:
            return jsonify({"error": "Project not found"}), 404
        
        db.session.delete(project)
        db.session.commit()
        
        return jsonify({"message": "Project deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

