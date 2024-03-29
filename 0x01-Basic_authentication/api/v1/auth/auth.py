#!/usr/bin/env python3
"""auth module"""
from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth"""
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p[-1] == '*':
                last = p.find('*')
                if path[:last] == p[:last]:
                    return False
            if p[-1] != '/':
                p += '/'
            if path == p:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """current_user"""
        return None
