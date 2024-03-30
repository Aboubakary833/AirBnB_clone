#!/usr/bin/python3
"""Define the Base for model classes."""
import uuid
import datetime
import models

time = datetime.datetime


class BaseModel:
    """BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = time.now()
            self.updated_at = time.now()
            #models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if (key == "id"):
                    self.id = value
                if ("created_at" == key):
                    self.created_at = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if ("updated_at" == key):
                    self.updated_at = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self) -> str:
        """toString equivalent for BaseModel

        Returns:
            str: a formatted string of the class
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += ("({}) {}".format(self.id, self.__dict__))
        return string

    def save(self):
        """Updates the public instance attribute updated_at
        """
        self.updated_at = time.now()
        #models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__

        Returns:
            __dict__: The instance __dict__ representation
        """
        __dict = self.__dict__.copy()
        __dict['__class__'] = self.__class__.__name__
        __dict["created_at"] = self.created_at.isoformat()
        __dict["updated_at"] = self.updated_at.isoformat()
        return __dict
