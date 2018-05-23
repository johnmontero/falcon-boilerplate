# -*- coding: utf-8 -*-
version_tuple = (0, 0, 1)

def get_version_string():
    if isinstance(version_tuple[-1], basestring):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))

__version__ = get_version_string()