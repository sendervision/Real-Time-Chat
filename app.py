import os
from dotenv import load_dotenv
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, send
from faker import Faker


load_dotenv()
MESSAGES = []

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY_APP')
socketio = SocketIO(app)

@app.route("/", methods=["GET", "POST"])
def main():
    name = Faker().name()
    user = {"username": name}
    return render_template("index.html", user=user, messages=MESSAGES)

@socketio.on('connect')
def connection(user):
    print("un nouveau utilisateur vient d'arriver")

@socketio.on('disconnect')
def disconnect():
    print("Un utilisateur vient de partir")

@socketio.on('send-msg')
def handle_message(msg):
    emit('recv-msg', msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)