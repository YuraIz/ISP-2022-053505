"""Fabrics that can create serializer."""
from serializers import xml_serializer, json_serializer
from serializers import yaml_serializer, serializer


class SerializerFabric:
    """Fabric that can create serializer."""

    def createSerializer() -> serializer.Serializer:
        """Create serializer."""
        pass


class XmlSerializerFabric(SerializerFabric):
    """Fabric that can create xml serializer."""

    def createSerializer() -> serializer.Serializer:
        """Create xml serializer."""
        return xml_serializer.XmlSerializer()


class JsonSerializerFabric(SerializerFabric):
    """Fabric that can create json serializer."""

    def createSerializer() -> serializer.Serializer:
        """Create json serializer."""
        return json_serializer.JsonSerializer()


class YamlSerializerFabric(SerializerFabric):
    """Fabric that can create xml serializer."""

    def createSerializer() -> serializer.Serializer:
        """Create yaml serializer."""
        return yaml_serializer.YamlSerializer()
