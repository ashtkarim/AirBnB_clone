#!/usr/bin/python3
"""
Module:place.py
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    class place
    """
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    amenity_ids = []
