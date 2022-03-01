import operator
import yaml

from pprint import pprint


class RangeNumbersException(Exception):
    def __init__(self, method: str):
        self.method = method


    def __str__(self) -> str:
        return f"Result of executing method '{self.method}' does not match the condition"


def parse_yaml(path: str) -> dict:
    with open(path, 'r') as stream:
        try:
            parsed_yaml = yaml.safe_load(stream)
            return parsed_yaml
        except yaml.YAMLError as ex:
            print(ex)


def validate_numbers(first_num: int, second_num: int, config: dict) -> None:
    for func, border in config.items():
        try:
            result = operator.methodcaller(func, first_num, second_num)(operator)
            if result <= border['max'] and result >= border['min']:
                print(result)
            else:
                raise RangeNumbersException(func)
        except RangeNumbersException as ex:
            # how can i replace type(ex).__name__ for output name of Exception???
            print(f"{type(ex).__name__}: {ex}")
        except AttributeError as ex:
            print(f"{type(ex).__name__}: {ex}")
            

if __name__ == '__main__':
    config = parse_yaml('data.yaml')
    pprint(config, sort_dicts=False)
    validate_numbers(40, 10, config)