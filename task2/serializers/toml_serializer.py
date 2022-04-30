"""Serialize objects, classes and functions to toml."""
import qtoml
import serializers.serializer_core as core
from serializers.serializer import Serializer


class TomlSerializer(Serializer):
    """Toml serializer."""

    def dumps(self, item):
        """Serialize object, class or function to toml."""
        return qtoml.dumps(core.serialize(item), encode_none=())

    def loads(self, string):
        """Deserialize object, class or function from toml."""
        return core.deserialize(qtoml.loads(string))
