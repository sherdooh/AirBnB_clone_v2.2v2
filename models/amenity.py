#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Represents an Amenity for a MySQL database
    """
    __tablename__ = "amenities"
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ''
