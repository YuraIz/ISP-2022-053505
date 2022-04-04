from types import MappingProxyType
from serializers.json_serializer import JsonSerializer


def mul(a, b):
    return a * b


def test_loads():
    serializer = JsonSerializer()
    s = serializer.dumps(serializer)
    serializer = serializer.loads(s)


def test_fun():
    serializer = JsonSerializer()
    s = serializer.dumps(mul)
    res = serializer.loads(s)
    assert res(6, 8) == 8*6


def test_mpt():
    serializer = JsonSerializer()
    item = {'key': 8, 'second_key': 9}
    mpt = MappingProxyType(item)
    s = serializer.dumps(mpt)
    res = serializer.loads(s)
