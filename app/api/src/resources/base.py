## coding: utf-8
import json
import falcon
from falcon import errors
from api.src.decorators.method_exception import method_exception

class BaseResource(object):

    def __init__(self, context, **kwargs):
        self.context = context
        for key, value in kwargs.items():
            setattr(self, key, value)


class CollectionResource(BaseResource):

    @method_exception
    def on_get(self, req, resp, *args, **kwargs):
        resp.media = []


class SingleResource(BaseResource):
    
    @method_exception
    def on_get(self, req, resp, *args, **kwargs):
        resp.media = {}
    
