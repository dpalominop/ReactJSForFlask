#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint

common_blueprint = Blueprint('common', __name__)

from . import views