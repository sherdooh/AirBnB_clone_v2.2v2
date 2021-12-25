#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from os import getenv
<<<<<<< HEAD
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
=======
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
>>>>>>> 96d932ff964b5c41b97f579bcd2e1b508fbbb4fe
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
<<<<<<< HEAD
    if models.storage_t == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City",  backref="state", cascade="delete")
    else:
        name = ""
=======
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",  backref="state",
                              cascade="all, delete, delete-orphan")
>>>>>>> 96d932ff964b5c41b97f579bcd2e1b508fbbb4fe

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
    
    if models.storage_t != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
