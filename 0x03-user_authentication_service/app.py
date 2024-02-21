#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home() -> str:
    """home route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """users route
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """the login route
    """
    if AUTH.valid_login(request.form.get('email'), request.form.get('password')):
        session_id = AUTH.create_session(request.form.get('email'))
        response = jsonify({"email": request.form.get('email'), "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
