import operator


def calculate(data: str) -> str:
    splited_data = data.split()
    try:
        func_name = splited_data[0]
        num1 = float(splited_data[1])
        num2 = float(splited_data[2])
        return str(operator.methodcaller(func_name, num1, num2)(operator))
    except ValueError as ex:
        return f"{type(ex).__name__}: {ex}"
    except AttributeError as ex:
        return f"{type(ex).__name__}: {ex}"
    except ZeroDivisionError as ex:
        return f"{type(ex).__name__}: {ex}"
    except IndexError as ex:
        return f"{type(ex).__name__}: {ex}"