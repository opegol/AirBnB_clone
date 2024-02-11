#!/usr/bin/python3

""" Definition of a User class for Airbnb Project"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel

    Attributes:
        email (string)
        password (string)
        first_name (string)
        last_name (string)
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
