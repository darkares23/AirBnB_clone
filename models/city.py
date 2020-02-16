#!/usr/bin/python3
"""
Module to inherit from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent the city an accommodation is located
    """
    state_id = ''
    name = ''
