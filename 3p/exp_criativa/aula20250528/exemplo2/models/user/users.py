#users.py
from models.db import db
from models.user.roles import Role
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer(), primary_key=True)
    role_id = db.Column( db.Integer, db.ForeignKey(Role.id))
    username= db.Column(db.String(45) , nullable=False, unique=True)
    email= db.Column(db.String(30), nullable=False, unique=True)
    password= db.Column(db.String(256) , nullable=False)
    
    def save_user(role_type_, username, email,password):
        role = Role.get_single_role(role_type_)
        user = User(role_id = role.id, username = username, email = email, password = generate_password_hash(password))
        db.session.add(user)
        db.session.commit()