"""
This Models module is used to create database schema
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.core.database import Base


def Project:
    id: int
    name: str
    description: str
    url: str
    completed: bool
