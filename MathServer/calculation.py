import operator 
import math


FUNCTIONS = {
    operator: {
        'add',
        'sub',
        'mul',
        'truediv',
        'mod',
    },

    math: {
        'copysign',
        'fmod',
        'ldexp',
        'pow',
    }
}


def calculate(data: str) -> dict:
    splited_data = data.split()
    try:
        func_name = splited_data[0]
        num1 = float(splited_data[1])
        num2 = float(splited_data[2])

        for pkg, funcs in FUNCTIONS.items():
            if func_name in funcs:
                return {
                    'operator': func_name,
                    'num1': num1,
                    'num2': num2,
                    'result': str(operator.methodcaller(func_name, num1, num2)(pkg))
                }
        
        # If function isn't found
        raise AttributeError("No such function.")

    except ValueError as ex:
        return f"{type(ex).__name__}: {ex}"
    except AttributeError as ex:
        return f"{type(ex).__name__}: {ex}"
    except ZeroDivisionError as ex:
        return f"{type(ex).__name__}: {ex}"
    except IndexError as ex:
        return f"{type(ex).__name__}: {ex}"