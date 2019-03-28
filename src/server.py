from flask import Flask
from flask_cors import CORS

import config
from route.common import common_blueprint
from route.notebook_instance import notebook_instance_blueprint

server = Flask(__name__)
server.debug = config.DEBUG

CORS(
    server,
    resource={r"/*": {"origins": "*"}},
    headers=['Content-Type', 'X-Requested-With', 'Authorization'],
)

server.register_blueprint(common_blueprint)
server.register_blueprint(notebook_instance_blueprint)

if __name__ == '__main__':
    server.run(host=config.HOST, port=config.PORT)
