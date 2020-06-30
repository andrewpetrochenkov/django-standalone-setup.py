import setuptools

setuptools.setup(
    name='django-standalone-setup',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
