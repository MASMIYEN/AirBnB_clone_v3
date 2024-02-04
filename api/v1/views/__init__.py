#!/usr/bin/python3
"""Blueprint API."""
from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.states import *

app_views = Blueprint('app_views', __name__)
'''blueprint for the AirBnB clone API'''
