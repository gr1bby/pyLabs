from typing import Union


class NumbersWrapper:
    def __init__(self, *args: Union[int, float]):
        self.__numbers = list(args)


    def __add__(self, other: 'NumbersWrapper') -> Union['IntsWrapper', 'FloatsWrapper']:
        first_list = self.__numbers
        second_list = other.numbers
        final_numbers = list()

        while len(first_list) < len(second_list):
            first_list.append(0)

        for item in range(len(first_list)):
            final_numbers.append(first_list[item] + second_list[item])

        for item in final_numbers:
            if isinstance(item, float):
                return FloatsWrapper(final_numbers)

        return IntsWrapper(final_numbers)


    def __sub__(self, other: 'NumbersWrapper') -> Union['IntsWrapper', 'FloatsWrapper']:
        first_list = self.__numbers
        second_list = other.numbers
        final_numbers = list()

        while len(first_list) < len(second_list):
            first_list.append(0)

        for item in range(len(first_list)):
            final_numbers.append(first_list[item] - second_list[item])

        for item in final_numbers:
            if isinstance(item, float):
                return FloatsWrapper(final_numbers)

        return IntsWrapper(final_numbers)


    def __mul__(self, other: 'NumbersWrapper') -> Union['IntsWrapper', 'FloatsWrapper']:
        first_list = self.__numbers
        second_list = other.numbers
        final_numbers = list()

        while len(first_list) < len(second_list):
            first_list.append(0)

        for item in range(len(first_list)):
            final_numbers.append(first_list[item] * second_list[item])

        for item in final_numbers:
            if isinstance(item, float):
                return FloatsWrapper(final_numbers)

        return IntsWrapper(final_numbers)


    def __div__(self, other: 'NumbersWrapper') -> Union['IntsWrapper', 'FloatsWrapper']:
        first_list = self.__numbers
        second_list = other.numbers
        final_numbers = list()

        while len(first_list) < len(second_list):
            first_list.append(0)

        for item in range(len(first_list)):
            final_numbers.append(first_list[item] / second_list[item])

        for item in final_numbers:
            if isinstance(item, float):
                return FloatsWrapper(final_numbers)

        return IntsWrapper(final_numbers)
    

    def __len__(self) -> int:
        return len(self.__numbers)


    def __setitem__(self, key: int, value: Union[int, float]) -> 'NumbersWrapper':
        new_list_of_numbers = self.__numbers
        new_list_of_numbers[key] = value
        return NumbersWrapper(new_list_of_numbers)


    def __delitem__(self, key: int) -> 'NumbersWrapper':
        new_list_of_numbers = self.__numbers
        del new_list_of_numbers[key]
        return NumbersWrapper(new_list_of_numbers)


    def __eq__(self, other: 'NumbersWrapper') -> bool:
        return self.numbers == other.numbers


    def __ne__(self, other: 'NumbersWrapper') -> bool:
        return self.numbers != other.numbers


    def __lt__(self, other: 'NumbersWrapper') -> bool:
        return sum(self.numbers) < sum(other.numbers)


    def __gt__(self, other: 'NumbersWrapper') -> bool:
        return sum(self.numbers) > sum(other.numbers)


    def __le__(self, other: 'NumbersWrapper') -> bool:
        return sum(self.numbers) <= sum(other.numbers)


    def __ge__(self, other: 'NumbersWrapper') -> bool:
        return sum(self.numbers) >= sum(other.numbers)


    def append(self, item: Union[int, float]) -> 'NumbersWrapper':
        return NumbersWrapper(self.numbers.append(item))


    @property
    def numbers(self) -> list:
        return self.__numbers


class IntsWrapper(NumbersWrapper):
    def __init__(self, *args: Union[int, float]):
        super().__init__(*args)


class FloatsWrapper(NumbersWrapper):
    def __init__(self, *args: Union[int, float]):
        super().__init__(*args)
