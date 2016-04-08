# -*- coding: utf-8 -*-
""" Url definitions for project."""

from views import wshandler, handle

routes = [
    ('GET', '/echo', wshandler),
    ('GET', '/{name}', handle)
]
