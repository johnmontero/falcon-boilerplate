import falcon
from falcon.http_error import HTTPError
from functools import wraps


def method_exception(method):
    """Decorator for exceptions."""
    @wraps(method)
    def method_wrapper(*args, **kwargs):
        try:
            method(*args, **kwargs)
        except Exception as error:
            raise HTTPError(description = str(error))

    return method_wrapper