#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
import sqlalchemy
import models
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
    if models.storage_t == "db":
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        __tablename__ = "cities"
        places = relationship("Place", backref="cities", cascade="delete")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
=======
    __tablename__ = "cities"
    if storage_type == 'db':
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete_orphan")
    else:
        name = ''
        state_id = ''
>>>>>>> 96d932ff964b5c41b97f579bcd2e1b508fbbb4fe
