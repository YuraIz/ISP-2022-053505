#!/usr/bin/python
"""How to use serializers."""


# TODO:
# [+] core
# [+] json
# [+] xml
# [+] yaml
# [ ] toml
# [ ] tests

from serializers.fabric import *


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
        print('Hello')


def some_thing(fabric: SerializerFabric):
    """Serialize and deserialize example object."""
    serializer = fabric.createSerializer()
    person = Person('tyler', 21)
    s = serializer.dumps(person)
    res = serializer.loads(s)
    res.greet()


some_thing(XmlSerializerFabric)
some_thing(JsonSerializerFabric)
some_thing(YamlSerializerFabric)
