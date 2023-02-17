from flask import Flask
from flask_restful import Api
from backend.config import DevelopmentConfig, ProductionConfig, Config

from api.users_api import TestHelloWorld


app = Flask(__name__)
api = Api(app, prefix='/api/')


if debug_app := Config.is_development_config():
    app.config.from_object(DevelopmentConfig())
else:
    app.config.from_object(ProductionConfig())


api.add_resource(TestHelloWorld, 'hello', methods=['GET'])


if __name__ == '__main__':
    app.run(port=8000, debug=debug_app)
