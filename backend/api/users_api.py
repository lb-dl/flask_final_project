from flask import current_app, jsonify
from flask_restful import Resource
from werkzeug.exceptions import BadRequest


class TestHelloWorld(Resource):
    def get(self):
        res = {'message': 'Hello, World!'}

        return res

    @staticmethod
    def register_routes():
        return ['hello']
