import os
from dotenv import load_dotenv
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit, send

from controllers.auth import _login, _logout, _signup
from database import USERS
from utils import verify_login

load_dotenv()
MESSAGES = []

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY_APP')
socketio = SocketIO(app)

@app.route("/")
@verify_login
def main():
    user = {"username": session.get("username")}
    users = USERS.keys()
    messages = [
        # {"user": "John", "message": "Bonjour à tous"},
        # {"user": "Jane", "message": "Comment ça va?"}
    ]
    return render_template("index.html", user=user, users=users, messages=MESSAGES)
    

@app.route("/signup", methods=["GET","POST"])
def signup():
    return _signup()

@app.route("/login", methods=["GET", "POST"])
def login():
    return _login()

@app.route('/logout')
def logout():
    return _logout()

@socketio.on('connect')
def connection(user):
    print("un nouveau utilisateur vient d'arriver")

@socketio.on('send-msg')
def handle_message(msg):
    emit('recv-msg', msg)
    print('received message: ', msg)

if __name__ == '__main__':
    socketio.run(app)