import serializers.serializer_core as core

from serializers.serializer import Serializer


class JsonSerializer(Serializer):

    def dumps(self, item):
        def to_str(item):
            if isinstance(item, dict):
                strings = list()
                for key, value in item.items():
                    strings.append(f'{to_str(key)}:{to_str(value)},')
                return f"{{{''.join(strings)[:-1]}}}"
            elif isinstance(item, str):
                s = item.translate(str.maketrans({
                    "\"":  r"\"",
                    "\\": r"\\",
                }))
                return f"\"{s}\""
            elif item is None:
                return 'null'
            else:
                return str(item)

        return to_str(core.serialize(item))

    def loads(self, string):
        null = None
        return core.deserialize(eval(string))
