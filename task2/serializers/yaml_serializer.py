"""Serialize objects, classes and functions to yaml."""
import serializers.serializer_core as core
from serializers.serializer import Serializer


class YamlSerializer(Serializer):
    """Yaml serializer."""

    def dumps(self, item):
        """Serialize object, class or function to yaml."""
        def to_str(item, depth=0):
            if isinstance(item, dict):
                strings = []
                prefix = '  '*depth
                prefix = '\n' + prefix
                for key, value in item.items():
                    strings.append(
                        f'{prefix}{to_str(key)}: {to_str(value, depth+1)}')
                return ''.join(strings)
            if isinstance(item, str):
                string = item.translate(str.maketrans({
                    "\"":  r"\"",
                    "\\": r"\\",
                }))
                return string
            if item is None:
                return ''
            return str(item)

        return to_str(core.serialize(item))

    def loads(self, string):
        """Deserialize object, class or function from yaml."""
        def get_sval(key: str, sval: str) -> any:
            res = sval

            if not key.endswith('bytes'):
                try:
                    if res.find('.') != -1:
                        res = float(res)
                    else:
                        res = int(res)
                except ValueError:
                    pass
            if res == '':
                res = None
            return res

        def iteration(string: str) -> any:
            res = {}
            splitted = string.split('\n')
            keys = list(
                filter((lambda a: a != '' and a[0] != ' '), splitted))
            end = 0
            dvals = []
            for i, key in enumerate(keys):
                start = splitted.index(key, end)
                if i == len(keys) - 1:
                    end = len(splitted)
                else:
                    end = splitted.index(keys[i + 1], start)
                dvals.append(list(splitted[start+1:end]))

            svals = [key.partition(': ')[2] for key in keys]
            keys = [key.partition(':')[0] for key in keys]
            dvals = ['\n'.join([s[2:] for s in e]) for e in dvals]

            for i, key in enumerate(keys):
                if len(dvals[i]) == 0:
                    res = res | {key: get_sval(key, svals[i])}
                else:
                    res = res | {key: iteration(dvals[i])}

            return res

        return core.deserialize(iteration(string))
