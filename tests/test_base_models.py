#!/usr/bin/python3
"""Test Base Model"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testpep8(unittest.TestCase):

    def test_pep8_conformance_base_model(self):
            """Test that we conform to PEP8."""
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(['models/base_model.py'])
            self.assertEqual(result.total_errors, 0, "Found style errors.")
