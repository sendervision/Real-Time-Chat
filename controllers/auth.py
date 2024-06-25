
from flask import redirect, url_for, render_template, request, session

from database import USERS
from utils import get_data_users, verify_password

def _signup():
    error_message = ""
    user = get_data_users()
    
    if user:
        if user.get("fullname") and user.get("username") and user.get("password"):
            if USERS.get(user["username"]):
                error_message ="Cette utilisateur existe"
            else:
                USERS[user["username"]] = {"password": user["password"]}
                return redirect(url_for("main"))
        else:
            error_message ="Donnée manquante"
    
    return render_template("signup.html", error=error_message)

def _login():
    if request.method == "GET":
        return render_template("login.html")
    
    user = get_data_users()
    if user and verify_password(user["username"], user["password"]):
        session['username'] = user["username"]
        USERS[user["username"]] = {"password": user["password"]}
        return redirect(url_for("main"))
    else:
        return render_template('login.html', error="Identifiant invalide")

def _logout():
    session.pop("username", None)
    return redirect(url_for('login'))
