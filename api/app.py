from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resource.user import UserAPI

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.debug = config.DEBUG
api = Api(app)

import models

api.add_resource(UserAPI, '/user')

if __name__ == '__main__':
    app.run(debug=True)

