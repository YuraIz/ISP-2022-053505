"""Fabrics that can create serializer."""
from abc import abstractmethod
import serializers


class SerializerFabric:
    """Fabric that can create serializer."""

    @staticmethod
    @abstractmethod
    def create_serializer() -> serializers.Serializer:
        """Create serializer."""

    @classmethod
    def check(cls):
        """Use serializer."""
        ser = cls.create_serializer()
        string = ser.dumps(cls)
        ser.loads(string)


class XmlSerializerFabric(SerializerFabric):
    """Fabric that can create xml serializer."""
    @staticmethod
    def create_serializer() -> serializers.Serializer:
        """Create xml serializer."""
        return serializers.XmlSerializer()


class JsonSerializerFabric(SerializerFabric):
    """Fabric that can create json serializer."""

    @staticmethod
    def create_serializer() -> serializers.Serializer:
        """Create json serializer."""
        return serializers.JsonSerializer()


class YamlSerializerFabric(SerializerFabric):
    """Fabric that can create xml serializer."""

    @staticmethod
    def create_serializer() -> serializers.Serializer:
        """Create yaml serializer."""
        return serializers.YamlSerializer()
