class Serializer:
    def dumps(self, item: any) -> str:
        pass

    def loads(self, string: str) -> any:
        pass

    def dump(self, item: any, filename: str):
        f = open(filename, 'w')
        f.write(self.dumps(item))

    def load(self, filename: str):
        f = open(filename, 'r')
        return self.loads(f.read())
