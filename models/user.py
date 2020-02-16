#!/usr/bin/python3
"""
Define User class
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Represent a site user and store their information
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
