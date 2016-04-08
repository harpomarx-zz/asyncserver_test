# -*- coding: utf-8 -*-
""" Main runner for asyncserver project. """

from aiohttp import web
from urls import routes
from aiohttp_jinja2 import setup
from jinja2 import FileSystemLoader
from settings import TEMPLATE_DIRECTORY


app = web.Application()
setup(app, loader=FileSystemLoader(TEMPLATE_DIRECTORY))
for route in routes:
    app.router.add_route(*route)

print('This is zie rooter')
print(dir(app.router))
print('And this is zie app')
print(dir(app))
web.run_app(app)
