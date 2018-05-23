# -*- coding: utf-8 -*-

import falcon

from api.src.middlewares.response_logger import ResponseLoggerMiddleware
from api.src.middlewares.require_jSON import RequireJSON
from api.src.middlewares.cors import CrossOriginResourceSharing
#
# Routers
from api.src.routers import CustomRouter

# Resources
from api.src.resources.user import UserCollection
from api.src.resources.user import UserSingle


class App(object):

    def __init__(self, ctx):
        self.ctx = ctx

        self.api = falcon.API(
            router=CustomRouter(),
            middleware=[
                CrossOriginResourceSharing(),
                RequireJSON(),
                ResponseLoggerMiddleware()
            ]
        )

        # load routes
        self._load_routes()

    def _load_routes(self):
        self.api.add_route('/users', UserCollection(self.ctx))
        self.api.add_route('/users/{id}', UserSingle(self.ctx))