#!/usr/bin/env python3.10
"""Setup cereal."""
from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='cereal',
    version='1.0',
    description='Application to serailize, deserialize and convert objects',
    author='YuraIz',
    packages=['cereal_modules', 'serializers'],
    scripts=['bin/cereal']
)
