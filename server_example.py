# -*- coding: utf-8 -*-
""" Main runner for asyncserver project. """

from aiohttp import web
from urls import routes


app = web.Application()
for route in routes:
    app.router.add_route(*route)

web.run_app(app)
