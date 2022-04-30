"""Tests for serializers.fabric module."""
from os import remove
from serializers.fabric import (
    SerializerFabric,
    XmlSerializerFabric,
    JsonSerializerFabric,
    YamlSerializerFabric,
    TomlSerializerFabric
)


def some_thing(fabric: SerializerFabric):
    """Check how serializer works."""
    item = ('test', 'another', {'key': 'val'}, None)
    serializer = fabric.create_serializer()
    serialized = serializer.dumps(item)
    res = serializer.loads(serialized)
    serializer.dump(res, 'testfile')
    res = serializer.load('testfile')
    assert res == item


def test_thing():
    """Check serializers."""
    some_thing(XmlSerializerFabric)
    some_thing(JsonSerializerFabric)
    some_thing(YamlSerializerFabric)
    remove('testfile')


def test_check():
    """Check that serializer works without exceptions."""
    XmlSerializerFabric.check()
    JsonSerializerFabric.check()
    YamlSerializerFabric.check()
    TomlSerializerFabric.check()
