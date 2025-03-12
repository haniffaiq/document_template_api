from flask import Blueprint, request, jsonify
from controllers.core.project_controller import *


# Create the Blueprint for the "projects" routes
project_bp = Blueprint('projects', __name__)

# Route to create a new project
@project_bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    return create_project(data)

# Route to get all projects
@project_bp.route('/', methods=['GET'])
def list_projects():
    return get_all_projects()

# Route to get a specific project by ID
@project_bp.route('/<int:project_id>', methods=['GET'])
def get_by_id(project_id):
    return get_project_by_id(project_id)

# Route to update a project by ID
@project_bp.route('/<int:project_id>', methods=['PUT'])
def update(project_id):
    data = request.get_json()
    return update_project(project_id, data)

# Route to delete a project by ID
@project_bp.route('/<int:project_id>', methods=['DELETE'])
def delete(project_id):
    return delete_project(project_id)
