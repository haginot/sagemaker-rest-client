from flask import jsonify
from flask_restful import Resource
import botostubs
from client.sagemaker_client import SageMakerClient


class ListNotebookInstance(Resource):

    def __init__(self):
        self.client: botostubs.SageMaker = SageMakerClient().client

    def get(self):
        res = self.client.list_notebook_instances()
        return jsonify(res)
