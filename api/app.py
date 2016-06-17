from flask import Flask
from flask_restful import Api
from resource.user import UserAPI
from resource.dump import DumpAPI
from models import db
import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.debug = config.DEBUG
api = Api(app)

api.add_resource(UserAPI, '/api/user')
api.add_resource(DumpAPI, '/api/dump')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
