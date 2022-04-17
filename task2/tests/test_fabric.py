from os import remove
from serializers.fabric import *


def some_thing(fabric: SerializerFabric):
    item = ('test', 'another', {'key': 'val'}, None)
    serializer = fabric.create_serializer()
    s = serializer.dumps(item)
    res = serializer.loads(s)
    serializer.dump(res, 'testfile')
    res = serializer.load('testfile')
    assert res == item


def test_thing():
    some_thing(XmlSerializerFabric)
    some_thing(JsonSerializerFabric)
    some_thing(YamlSerializerFabric)
    remove('testfile')
