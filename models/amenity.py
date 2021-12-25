#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
from os import getenv
import sqlalchemy
import models
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
=======
from models.base_model import Base, BaseModel
from models import storage_type
from sqlalchemy import Column, String
>>>>>>> 96d932ff964b5c41b97f579bcd2e1b508fbbb4fe
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Represents an Amenity for a MySQL database
    """
<<<<<<< HEAD
    if models.storage_t == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
=======
    __tablename__ = "amenities"
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ''
>>>>>>> 96d932ff964b5c41b97f579bcd2e1b508fbbb4fe
