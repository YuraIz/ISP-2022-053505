from construct import this
import serializer_core as core


class JsonSerializer:

    def dumps(self, item: any) -> str:
        def to_str(dictionary: dict[str, any]):
            return str(dictionary).replace("'", '"').replace('None', 'null')
        return to_str(core.serialize(item))

    def try_to_load(self, string) -> any:
        def to_str(dictionary: dict[str, any]):
            return str(dictionary).replace('null', 'None')
        return core.deserialize(eval(to_str(string)))
