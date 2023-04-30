"""
This module include all the dependencies that are required for the application
"""
from functools import lru_cache

from app.core.config import settings  # Settings is added
from app.core.security import get_password_hash


def get_settings():
    return settings


@lru_cache()
def get_password_hasher():
    return get_password_hash
