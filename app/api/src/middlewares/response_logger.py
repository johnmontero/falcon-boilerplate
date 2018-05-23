import falcon
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class ResponseLoggerMiddleware(object):
    def process_response(self, req, resp, resource, req_succeeded):
        logger.info('{0} {1} {2}'.format(req.method, req.relative_uri, resp.status[:3]))