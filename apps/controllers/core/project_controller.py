from flask import request, jsonify
from models.core.project import Project, db
from datetime import datetime

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

def get_project_by_id(id):
    try:
        # Fetch the project by ID
        project = Project.query.get(id)
        
        # If project not found, return 404 error
        if not project:
            return jsonify({"error": "Project not found"}), 404
        
        return jsonify(project.as_dict()), 200
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

