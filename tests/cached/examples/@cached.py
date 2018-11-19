#!/usr/bin/env python
from cached import cached


@cached
def func():
    print("log")

func()
func()  # CACHED!
