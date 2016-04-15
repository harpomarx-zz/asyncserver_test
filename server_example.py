# -*- coding: utf-8 -*-
""" Main runner for asyncserver project. """

from aiohttp import web
from urls import routes
from aiohttp_jinja2 import setup
from jinja2 import FileSystemLoader
from settings import TEMPLATE_DIRECTORY
# import api_hour


app = web.Application()
setup(app, loader=FileSystemLoader(TEMPLATE_DIRECTORY))
for route in routes:
    app.router.add_route(*route)

web.run_app(app)


'''
class Container(api_hour.Container):
    """ Test API hour container"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Declare HTTP server
        self.servers['http'] = app
        self.servers['http'].ah_container = self  # keep a reference in HTTP server to Container

    async def start(self):
        """

        :return:
        """
        # A coroutine called when the Container is started
        return super().start()

    async def stop(self):
        """

        :return:
        """
        # A coroutine called when the Container is stopped
        return super().stop()

    def make_servers(self):
        """

        :return:
        """
        # This method is used by api_hour command line to bind your HTTP server on socket
        return [self.servers['http'].make_handler(logger=self.worker.log,
                                                  keep_alive=self.worker.cfg.keepalive,
                                                  access_log=self.worker.log.access_log,
                                                  access_log_format=self.worker.cfg.access_log_format)]
'''
