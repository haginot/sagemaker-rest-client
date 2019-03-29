from flask import Flask
from flask_cors import CORS

import config
from client.sagemaker_client import SageMakerClient
from route.common import common_blueprint
from route.notebook_instance import notebook_instance_blueprint

server = Flask(__name__)
CORS(server)

server.debug = config.DEBUG
server.config['AWS_SESSION'] = config.AWS_SESSION
client = SageMakerClient(**server.config['AWS_SESSION'])

server.register_blueprint(common_blueprint)
server.register_blueprint(notebook_instance_blueprint)

if __name__ == '__main__':
    server.run(host=config.HOST, port=config.PORT)
