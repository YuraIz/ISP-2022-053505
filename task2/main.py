#!/usr/bin/python

# TODO:
# [+] serialize functions
# [ ] serialize objects
# [ ] serialize objects with functions
# [ ] serialize classes


import json

from matplotlib.font_manager import json_load

from serializer_core import deserialize

from json_serializer import JsonSerializer


def mul(a, b):
    return a * b


test_tuple = (1, 'hello')


class Person:
    name: str
    age: int

    def get_age():
        return 6

    def greet():
        print('Hello')


jserializer = JsonSerializer()

s = jserializer.dumps(Person)
print(jserializer.try_to_load(s))
multip = deserialize(json.loads(s))
