import json
import falcon
from falcon.media.validators.jsonschema import validate

from api.src.resources.base import CollectionResource
from api.src.resources.base import SingleResource
from api.src.schemas import load_schema

PERSONAL_DATA =  [
    {"id":1, "name":"John"},
    {"id":2, "name":"Ronald"},
    {"id":3, "name":"Francis"},
    {"id":4, "name":"Alfredo"}
]

class UserCollection(CollectionResource):

    def on_get(self, req, resp, **kwargs):
        super(UserCollection, self).on_get(req, resp, **kwargs)
        results = PERSONAL_DATA
        resp.media = results

    @validate(load_schema('user_creation'))
    def on_post(self, req, resp, **kwargs):
        result = {
            'username': req.media.get('username'),
            'name': req.media.get('name')
        }
        resp.status = falcon.HTTP_201
        resp.media = result
        

class UserSingle(SingleResource):

    def on_get(self, req, resp, **kwargs):
        super(UserSingle, self).on_get(req, resp, **kwargs)
        result = { "id": kwargs['id']}
        resp.body = json.dumps(result)

    @validate(load_schema('user_creation'))
    def on_put(self, req, resp, **kwargs):
        result = {
            "id": kwargs['id'],
            'username': req.media.get('username'),
            'name': req.media.get('name')
        }
        resp.status = falcon.HTTP_201
        resp.media = result

    def on_delete(self, req, resp, **kwargs):
        result = { 
            "id": kwargs['id'],
            "method": req.method.upper()
            }
        resp.body = json.dumps(result)