class TypeValidationError(Exception):
    def __init__(self, param, expected_type):
        self.param  = param
        self.expected_type = expected_type


    def __str__(self):
        return f"Expected type is {self.expected_type}. This type is {type(self.param)}"


def validate_args(function):

    def wrapper(*args):
        i = 0
        expected_types = function.__annotations__.values()
        for t in expected_types:
            if not isinstance(args[i], t):
                raise TypeValidationError(args[i], t)
            i += 1

        function(*args)

    return wrapper


@validate_args
def func(a: str, b: int, c: dict):
    print("This good")
    

if __name__ == '__main__':
    func('1', 2, {'3', 4})
