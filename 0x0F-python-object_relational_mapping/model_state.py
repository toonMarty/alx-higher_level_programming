#!/usr/bin/python3
"""
This module contains the class definition of a state and an
instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """The class State that will link to MySQL table states"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
