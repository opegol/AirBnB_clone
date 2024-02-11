#!/usr/bin/python3

""" Definition of a State class for Airbnb Project"""


from models.base_model import BaseModel


class State(BaseModel):
    """State class inherits from BaseModel

    Attributes:
        name (string) - name of state
    """

    name = ''
