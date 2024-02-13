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
        if self.authorization_header(request) is None or\
            not self.authorization_header(request).startswith('Basic ') or\
                not isinstance(self.authorization_header(request), str):
            return None
        return base64.b64encode(self.authorization_header(request)[6:].encode()).decode()
