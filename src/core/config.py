import os
from authx import AuthX, AuthXConfig
from datetime import timedelta


def get_security() -> AuthX:
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        raise ValueError("SECRET_KEY environment variable not set")

    config = AuthXConfig(
        JWT_SECRET_KEY=secret_key,
        JWT_ALGORITHM="HS256",
        JWT_ACCESS_TOKEN_EXPIRES=timedelta(seconds = 3600),
    )

    return AuthX(config)