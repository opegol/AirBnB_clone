#!/usr/bin/python3

""" Definition of a Place class for Airbnb Project"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Place class inherits from BaseModel

    Attributes:
        city_id (string) - it will be the City.id
        user_id (string) - it will be the User.id
        name (string) - name of place
        description (string) - description of place
        number_rooms (integer) - number of rooms in place
        number_bathrooms (integer) - number of bathrooms in place
        max_guest (integer) - maximum guests that can be accommodated
        price_by_night (integer) - price by night at place
        latitude (float) - latitude of place
        longitude (float) - longitude of place
        amenity_ids (list of string) - it will be the list of Amenity.id
    """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
