# -*- coding: utf-8 -*-
""" Settings for asyncserver."""

import os

CONFIG_PATH = os.path.realpath(__file__)
SRC_DIRECTORY = os.path.dirname(CONFIG_PATH)

TEMPLATE_DIRECTORY = os.path.join(SRC_DIRECTORY, 'templates')
