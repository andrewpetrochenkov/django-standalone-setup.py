[![](https://img.shields.io/pypi/pyversions/cached.svg?longCache=True)](https://pypi.org/pypi/cached/)
[![](https://img.shields.io/pypi/v/cached.svg?maxAge=3600)](https://pypi.org/pypi/cached/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/cached.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/cached.py/)

#### Install
```bash
$ [sudo] pip install cached
```

#### Functions
function|description
-|-
`cached.cached(function)`|`@cache` decorator, `cache(function)` - cache function result

#### Examples
`@cached` decorator

```python
>>> from cached import cached

>>> @cached
    def func(*args, **kwags):
```

`cached(function)` function
```python
>>> from cached import cached

>>> def func(*args, **kwags):
        ...
>>> cached(func)()
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>