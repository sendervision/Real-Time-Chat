from functools import wraps
from flask import session, redirect, url_for, request

from database import USERS

def verify_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) if session.get('username') else redirect(url_for('login'))
    return wrapper

def get_data_users() -> dict:
    if request.method == "POST" and request.form:
        fullname = request.form.get("fullname")
        username = request.form.get("email")
        password = request.form.get("password")
        return {"fullname": fullname, "username": username, "password": password}
    return

def verify_password(username, password):
    return username in USERS and USERS[username]["password"] == password
