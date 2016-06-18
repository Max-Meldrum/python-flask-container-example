from app import db
from models import User

db.create_all()

user = User('enya')
user.hash_password('secret')
db.session.add(user)
db.session.commit()
print("User created!")
