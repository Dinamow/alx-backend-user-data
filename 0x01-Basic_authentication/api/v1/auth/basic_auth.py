#!/usr/bin/env python3
"""basic auth module"""
from api.v1.auth.auth import Auth
import base64
from flask import request


class BasicAuth(Auth):
    """basic auth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract base64 authorization header"""
        if authorization_header is None or\
            not isinstance(authorization_header, str)or\
                not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """decode base64 authorization header"""
        if base64_authorization_header is None or\
            not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None
