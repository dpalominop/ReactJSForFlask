#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)


def create_app():
    from common import common_blueprint
    app.register_blueprint(common_blueprint)
    return app