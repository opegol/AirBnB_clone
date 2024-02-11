#!/usr/bin/python3

""" Definition of a Review class for Airbnb Project"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel

    Attributes:
        place_id (string) - it will be the Place.id
        user_id (string) - it will be the User.id
        text (string) - text of review
    """

    place_id = ''
    user_id = ''
    text = ''
