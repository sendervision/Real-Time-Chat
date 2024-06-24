from functools import wraps
from flask import Flask, render_template, redirect, request, url_for, session
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

users = {
    "john": {"password": "hello"},
    "susan": {"password": "bye"}
}

def verify_password(username, password):
    return username in users and users[username]["password"] == password

def checkConnectionUser(func):
    @wraps(func)
    def check(*args, **kwargs):
        return render_template("index.html") if 'username' in session else func(*args, **kwargs)
    return check

@app.route("/")
@checkConnectionUser
def main():
    return redirect(url_for('login'))

@app.route("/signup")
@checkConnectionUser
def signup():
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
@checkConnectionUser
def login():
    if request.method == "POST" and request.form:
        username = request.form.get("username")
        password = request.form.get("password")
        if verify_password(username, password):
            session['username'] = username
            return redirect(url_for('main'))
        else:
            return render_template('login.html', error="Identifiant invalide")
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for('login'))

@socketio.on('connect')
def connection(user):
    print(user)
    print("un nouveau utilisateur vient d'arriver")

@socketio.on('event')
def handle_message(json):
    print('received message: ', json)

if __name__ == '__main__':
    socketio.run(app)