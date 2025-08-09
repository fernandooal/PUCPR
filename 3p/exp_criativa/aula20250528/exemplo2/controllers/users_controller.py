#users_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from models.user.users import User
from models.user.roles import Role

user = Blueprint("user", __name__ , template_folder="views")

@user.route('/register_user')
def register_user():
    roles = Role.get_role()
    return render_template("register_user.html", roles=roles)

@user.route('/add_user', methods=['POST'])
def add_user():
    global users
    if request.method == 'POST':
        role_name = request.form['role_type_']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        User.save_user(role_name, username, email,password)
        return render_template("home.html")

