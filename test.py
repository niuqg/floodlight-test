from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self, id):
        pass
    def put(self, id):
        pass
    def delete(self, id):
        pass

class Users(Resource):
    def get(self):
        pass
    def post(self):
        pass

api.add_resource(User, '/users/<int:id>', endpoint='user')
api.add_resource(Users, '/users', endpoint='users')
