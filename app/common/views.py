#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import render_template

from . import common_blueprint


@common_blueprint.route('/')
def index():
    return render_template('common/index.html')