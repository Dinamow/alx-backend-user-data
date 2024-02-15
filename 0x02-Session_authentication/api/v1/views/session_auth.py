#!/usr/bin/env python3
""" Module of Session authentication views
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session() -> str:
    """ POST /auth_session/login
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    if not User.search({'email': email}):
        return jsonify({"error": "no user found for this email"}), 404

    for user in User.search({'email': email}):
        from api.v1.app import auth
        if user.is_valid_password(password):
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            response.set_cookie('session_id', session_id)
            return response
    return jsonify({"error": "wrong password"}), 401