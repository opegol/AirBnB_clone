#!/usr/bin/python3

""" Definition of a City class for Airbnb Project"""


from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel

    Attributes:
        state_id (string) - it will be the State.id
        name (string) - name of city
    """

    state_id = ''
    name = ''
