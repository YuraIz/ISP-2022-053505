"""Abstract serializer."""


from abc import abstractmethod


class Serializer:
    """Abstract serializer."""

    @abstractmethod
    def dumps(self, item: any) -> str:
        """Serialize object, class or function."""
        return

    @abstractmethod
    def loads(self, string: str) -> any:
        """Deserialize object, class or function."""
        return

    def dump(self, item: any, filename: str):
        """Serialize object, class or function and write to file."""
        with open(filename, 'w', encoding='utf8') as file:
            file.write(self.dumps(item))

    def load(self, filename: str):
        """Read from file and deserialize object, class or function."""
        with open(filename, 'r', encoding='utf8') as file:
            string = file.read()
        return self.loads(string)
