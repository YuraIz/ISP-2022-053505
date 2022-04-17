#!/usr/bin/python
"""How to use serializers."""


# TODO:
# [+] core
# [+] json
# [+] xml
# [+] yaml
# [ ] toml
# [ ] tests

from serializers.fabric import (SerializerFabric, XmlSerializerFabric,
                                JsonSerializerFabric, YamlSerializerFabric)

import serializers.serializer_core as core

globals().update(core.__dict__)


class Person:
    """Example class."""

    def __init__(self, name='test', age=32) -> None:
        """Initialize."""
        self.name = name
        self.age = age

    name: str
    age: int

    def get_age(self):
        """Return age of person.."""
        return self.age

    def greet(self):
        """Say hello."""
        print(f'Hello, my name is {self.name}')


def some_thing(fabric: SerializerFabric):
    """Serialize and deserialize example object."""
    serializer = fabric.create_serializer()
    person = Person('tyler', 21)
    string = serializer.dumps(person)
    res = serializer.loads(string)
    res.greet()

    print(isinstance(res, Person))


some_thing(XmlSerializerFabric)
some_thing(JsonSerializerFabric)
some_thing(YamlSerializerFabric)
