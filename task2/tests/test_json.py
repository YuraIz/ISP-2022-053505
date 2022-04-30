"""Tests for JsonSerializer."""
from types import MappingProxyType
from serializers.json_serializer import JsonSerializer


def mul(first, second):
    """Function to check."""
    return first * second


def test_loads():
    """Dumps and loads works without exeptions."""
    serializer = JsonSerializer()
    serialized = serializer.dumps(serializer)
    serializer = serializer.loads(serialized)


def test_fun():
    """Function dumps and loads correct."""
    serializer = JsonSerializer()
    serialized = serializer.dumps(mul)
    res = serializer.loads(serialized)
    assert res(6, 8) == 8*6


def test_mpt():
    """Serializer can work with MappingProxyType."""
    serializer = JsonSerializer()
    item = {'key': 8, 'second_key': 9}
    mpt = MappingProxyType(item)
    serialized = serializer.dumps(mpt)
    serializer.loads(serialized)
