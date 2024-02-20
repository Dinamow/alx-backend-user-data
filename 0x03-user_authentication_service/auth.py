#!/usr/bin/env python3
"""
auth module
"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """Takes in a password string arguments and returns a salted, hashed password
    """
    return hashpw(password.encode(), gensalt())