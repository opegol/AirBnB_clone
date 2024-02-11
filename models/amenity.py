#!/usr/bin/python3

""" Definition of a Amenity class for Airbnb Project"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel

    Attributes:
        name (string) - name of amenity
    """

    name = ''
