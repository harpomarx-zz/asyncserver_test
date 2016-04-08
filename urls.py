# -*- coding: utf-8 -*-
""" Url definitions for project."""

from views import wshandler, handle, template_handler

routes = [
    ('GET', '/echo', wshandler),
    ('GET', '/{name}/', handle),
    ('GET', '/test_template', template_handler)
]
