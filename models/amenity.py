#!/usr/bin/python3
"""
Module to inherit from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represent the amenities of an accommodation
    """
    name = ''
