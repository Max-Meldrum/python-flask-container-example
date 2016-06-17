from flask_restful import Resource, reqparse
from flask import abort, g
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
# cred to http://blog.miguelgrinberg.com/post/restful-authentication-with-flask


class UserAPI(Resource):
    """API resource for users."""

    @auth.login_required
    def get(self):
        return "hello " + auth.username()

    def post(self):
        """Creating API user."""
        from models import User
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help="Name cannot be blank")
        parser.add_argument('password', required=True, help="Enter password")
        args = parser.parse_args()
        name = args['name']
        password = args['password']
        if User.query.filter_by(name=name).first() is not None:
            abort(400)
        user = User(name=name)
        user.hash_password(password)
        from app import db
        db.session.add(user)
        db.session.commit()
        return "User created!"

    def verify_password(username, password):
        user = User.query.filter_by(name=username).first()
        if not user or not user.verify_password(password):
            return False
        g.user = user
        return True
