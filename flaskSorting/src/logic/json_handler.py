import orjson


class JSONEncoder:
    def __init__(self, **kwargs):
        self.options = kwargs


    def encode(self, obj):
        return orjson.dumps(obj).decode('utf-8')


class JSONDecoder:
    def __init__(self, **kwargs):
        self.options = kwargs


    def decode(self, obj):
        return orjson.loads(obj)
