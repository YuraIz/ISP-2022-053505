#!/usr/bin/python

# TODO:
# [+] core
# [+] json
# [+] xml
# [+] yaml
# [ ] toml
# [ ] tests

from types import NoneType
from serializers.fabric import *


class Person:
    def __init__(self, name='test', age=32) -> None:
        self.name = name
        self.age = age

    name: str
    age: int

    def get_age(self):
        return self.age

    def greet(self):
        print('Hello')


def some_thing(fabric: SerializerFabric):
    serializer = fabric.createSerializer()
    person = Person('tyler', 21)
    s = serializer.dumps(person)
    res = serializer.loads(s)
    res.greet()


some_thing(XmlSerializerFabric)
some_thing(JsonSerializerFabric)
some_thing(YamlSerializerFabric)
