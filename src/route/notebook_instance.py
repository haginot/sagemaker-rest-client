from flask import Blueprint
from flask_restful import Api
from resource.notebook_instance import ListNotebookInstance

notebook_instance_blueprint = Blueprint('notebook_instance', __name__)
notebook_instance_blueprint_api = Api(notebook_instance_blueprint)

notebook_instance_blueprint_api.add_resource(ListNotebookInstance, '/notebook_instance')
