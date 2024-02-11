#!/usr/bin/python3

"""Definition of BaseModel class"""
import json
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class for Airbnb project"""

    def __init__(self, *args, **kwargs):
        """Initializes a Base class

        Args:
            *args - tuple containing attribute values (will not be used)
            **kwargs - dictionary containing attribute and value pairs

        id (str) - unique id assign with uuid when an instance is created
        created_at (datetime) - assigned with the current datetime when \
                an instance is created
        updated_at (datetime) - assigned with the current datetime when \
                an instance is created and it will be updated whenever \
                object is changed
        """
        if kwargs:
            for arg in kwargs.keys():
                if arg != '__class__':
                    if arg in ('created_at', 'updated_at'):
                        setattr(self, arg, datetime.strptime(kwargs[arg],
                                '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, arg, kwargs[arg])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a str format for a BaseModel object"""
        # bm_str = "[" + str(self.__class__.__name__) + "] (" + str(self.id) \
        #       + ") " + str(self.__dict__)
        bm_str = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return bm_str

    def save(self):
        """updates the attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
            __dict__ of the instance.
        """
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = (self.created_at).isoformat()
        dct['updated_at'] = (self.updated_at).isoformat()
        return dct
