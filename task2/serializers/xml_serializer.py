"""Serialize objects, classes and functions to yaml."""
import serializers.serializer_core as core
from serializers.serializer import Serializer


class XmlSerializer(Serializer):
    """Xml serializer."""

    def dumps(self, item):
        """Serialize object, class or function to xml."""
        def to_str(item):
            if isinstance(item, dict):
                strings = []
                for key, value in item.items():
                    strings.append(f"<{key}>{to_str(value)}</{key}>")
                return ''.join(strings)
            if item is None:
                return '<null />'
            return str(item)

        return to_str(core.serialize(item))

    def loads(self, string):
        """Deserialize object, class or function from xml."""
        def iteration(string: str) -> tuple[str, any, str | None]:
            key = string.partition('>')[0][1:]
            if '<' in key:
                res = string.partition('<')[0]
                if not key.endswith('bytes'):
                    try:
                        if res.find('.') != -1:
                            res = float(res)
                        else:
                            res = int(res)
                    except ValueError:
                        pass
                return (None, res, string.partition('>')[2])
            if '>' not in string:
                return (None, string, None)
            if key == "null /":
                return (None, None, string.partition('>')[2].partition('>')[2])
            if key.startswith('/'):
                return (None, None, string.partition('>')[2])

            value = string.removeprefix(f"<{key}>").removesuffix(f"</{key}>")
            itres = iteration(value)

            if itres[0] is None:
                return (key, itres[1], itres[2])
            dictionary = {itres[0]: itres[1]}
            while itres[2] is not None:
                itres = iteration(itres[2])
                if itres[0] is None:
                    break
                dictionary = dictionary | {itres[0]: itres[1]}
            return (key, dictionary, itres[2])

        key, value, _ = iteration(string)
        return core.deserialize({key: value})
