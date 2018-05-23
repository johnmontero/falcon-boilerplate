import datetime
import decimal


def json_serializer(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    elif isinstance(obj, decimal.Decimal):
        return str(obj)

    raise TypeError('Cannot serialize {!r} (type {})'.format(obj, type(obj)))