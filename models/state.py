#!/usr/bin/python3
"""
Module to inherit from BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inhiret BaseModel
    """
    email=''
    password=''
    first_name=''
    last_name=''
