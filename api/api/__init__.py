import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("users.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

class UserList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            devices.append(shelf[key])

        return {'message': 'Success', 'data': devices}, 200

    def post(self):
        import re
        parser = reqparse.RequestParser()

        parser.add_argument('username', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('address', required=True)
        parser.add_argument('birthday', required=True)

       
        # Parse the arguments into an object
        args = parser.parse_args()
        
        bdayReg = "^((0?[13578]|10|12)(-|\/)(([1-9])|(0[1-9])|([12])([0-9]?)|(3[01]?))(-|\/)((19)([2-9])(\d{1})|(20)([01])(\d{1})|([8901])(\d{1}))|(0?[2469]|11)(-|\/)(([1-9])|(0[1-9])|([12])([0-9]?)|(3[0]?))(-|\/)((19)([2-9])(\d{1})|(20)([01])(\d{1})|([8901])(\d{1})))$"
        if re.match(bdayReg,args["birthday"] ) == None:
            return {'message': 'Invalid Birthday' }, 400

        shelf = get_db()
        shelf[args['username']] = args

        return {'message': 'User Registered', 'data': args}, 201




api.add_resource(UserList, '/users')




