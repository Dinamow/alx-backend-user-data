#!/usr/bin/env python3
"""auth module"""
from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] == '/':
            return False
        for i in excluded_paths:
            if i[-1] == '/':
                if i[:-1] == path:
                    return False
            else:
                if i == path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        return None

    def current_user(self, request=None) -> User:
        """current_user"""
        return None
