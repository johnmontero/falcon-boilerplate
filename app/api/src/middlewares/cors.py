class CrossOriginResourceSharing(object):

    def process_request(self, req, resp):
        header = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE'
        }
        resp.set_headers(header)
