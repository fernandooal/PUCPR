from flask import Flask
from sqlalchemy import text
from models import db
from models.user.roles import Role
from models.user.users import User

def create_db(app: Flask):
    with app.app_context():
        db.session.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
        db.session.commit()

        db.drop_all()
        db.create_all()
        
        Role.save_role( "Admin", "Usuário full" )
        Role.save_role( "User", "Usuário com limitações")
        
        User.save_user("Admin","Admin", "admin","admin")

        db.session.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
        db.session.commit()
