import re
from os.path import join, dirname

from setuptools import setup, find_packages


with open(join(dirname(__file__), 'card_holder', '__init__.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S)\
        .match(v_file.read()).group(1)


dependencies = [
    'restfulpy >= 2.6.14',
]


setup(
    name='card_holder',
    author='mrastiak',
    author_email='armin.ayari@gmail.com',
    version=package_version,
    install_requires=dependencies,
    packages=find_packages(),
    test_suite='card_holder.tests',
    entry_points={
        'console_scripts': [
            'card_holder = card_holder:card_holder.cli_main'
        ]
    }
)

