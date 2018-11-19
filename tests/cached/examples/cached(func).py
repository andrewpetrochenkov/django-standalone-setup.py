#!/usr/bin/env python
from cached import cached


def func(*args, **kwargs):
    print("args = %s, kwargs= %s" % (args, kwargs))

cached(func)("arg", kwarg="value")
cached(func)("arg", kwarg="value")  # CACHED!
