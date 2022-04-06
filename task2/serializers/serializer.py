"""Abstract serializer."""


class Serializer:
    """Abstract serializer."""

    def dumps(self, item: any) -> str:
        """Serialize object, class or function."""
        pass

    def loads(self, string: str) -> any:
        """Deserialize object, class or function."""
        pass

    def dump(self, item: any, filename: str):
        """Serialize object, class or function and write to file."""
        f = open(filename, 'w')
        f.write(self.dumps(item))

    def load(self, filename: str):
        """Read from file and deserialize object, class or function."""
        f = open(filename, 'r')
        return self.loads(f.read())
