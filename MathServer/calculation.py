import operator 
import math


FUNCTIONS = {
    operator: [
        'add',
        'sub',
        'mul',
        'truediv',
        'mod',
    ],

    math: [
        'copysign',
        'fmod',
        'ldexp',
        'pow',
    ]
}


def calculate(data: str) -> str:
    splited_data = data.split()
    try:
        func_name = splited_data[0]
        num1 = float(splited_data[1])
        num2 = float(splited_data[2])
        
        if func_name in FUNCTIONS[operator]:
            result = operator.methodcaller(func_name, num1, num2)(operator)

        elif func_name in FUNCTIONS[math]:
            result = operator.methodcaller(func_name, num1, num2)(math)

        else:
            raise AttributeError("No such function.")

        return str(result)
    except ValueError as ex:
        return f"{type(ex).__name__}: {ex}"
    except AttributeError as ex:
        return f"{type(ex).__name__}: {ex}"
    except ZeroDivisionError as ex:
        return f"{type(ex).__name__}: {ex}"
    except IndexError as ex:
        return f"{type(ex).__name__}: {ex}"