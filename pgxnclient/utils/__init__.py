"""
pgxnclient -- misc utilities package
"""

# Copyright (C) 2011-2018 Daniele Varrazzo

# This file is part of the PGXN client


__all__ = ['load_json', 'load_jsons', 'sha1', 'find_executable']


import os
import json
from collections import OrderedDict

# Import the sha1 object without warnings
from hashlib import sha1

import six


def load_json(f):
    data = f.read()
    if not isinstance(data, six.text_type):
        data = data.decode('utf-8')
    return load_jsons(data)


def load_jsons(data):
    return json.loads(data, object_pairs_hook=OrderedDict)


def find_executable(name):
    """
    Find executable by ``name`` by inspecting PATH environment variable, return
    ``None`` if nothing found.
    """
    for dir in os.environ.get('PATH', '').split(os.pathsep):
        if not dir:
            continue
        fn = os.path.abspath(os.path.join(dir, name))
        if os.path.exists(fn):
            return os.path.abspath(fn)
