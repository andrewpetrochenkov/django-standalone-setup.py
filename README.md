[![](https://img.shields.io/pypi/pyversions/django-standalone-setup.svg?longCache=True)](https://pypi.org/project/django-standalone-setup/)
[![](https://img.shields.io/pypi/v/django-standalone-setup.svg?maxAge=3600)](https://pypi.org/project/django-standalone-setup/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/django-standalone-setup.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/django-standalone-setup.py/)

#### Install
```bash
$ [sudo] pip install django-standalone-setup
```

#### Features
calls `django.setup` once only

#### Config
```bash
$ export DJANGO_SETTINGS_MOULE='django_settings'
```

`site-package/django_settings.py`
```python
INSTALLED_APPS = [
    'your_app',
]
DATABASES = {
    'default': {
        ...
    }
}
```

#### Examples
`script.py`
```python
# !/usr/bin/env python
import django_standalone_setup # at the top of module
...
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>