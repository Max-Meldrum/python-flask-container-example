from flask import Flask
from flask_restful import Api
from resource.user import User

import config

app = Flask(__name__)
app.debug = config.DEBUG
api = Api(app)


api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True)
