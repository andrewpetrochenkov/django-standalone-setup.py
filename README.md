<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-standalone-setup.svg?maxAge=3600)](https://pypi.org/project/django-standalone-setup/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-standalone-setup.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-standalone-setup.py/actions)

### Installation
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

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
