from flask_restful import Resource


class UserAPI(Resource):
    def get(self):
        return "hello"
