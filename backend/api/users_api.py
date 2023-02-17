from flask_restful import Resource


class TestHelloWorld(Resource):
    def get(self):
        res = {'message': 'Hello, World!'}

        return res

    @staticmethod
    def register_routes():
        return ['hello']
