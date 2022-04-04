from serializers import xml_serializer, json_serializer
from serializers import yaml_serializer, serializer


class SerializerFabric:
    def createSerializer() -> serializer.Serializer:
        pass


class XmlSerializerFabric(SerializerFabric):
    def createSerializer() -> serializer.Serializer:
        return xml_serializer.XmlSerializer()


class JsonSerializerFabric(SerializerFabric):
    def createSerializer() -> serializer.Serializer:
        return json_serializer.JsonSerializer()


class YamlSerializerFabric(SerializerFabric):
    def createSerializer() -> serializer.Serializer:
        return yaml_serializer.YamlSerializer()
