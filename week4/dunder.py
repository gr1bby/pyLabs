class Number:

    def __get__(self, instance, owner):
        return instance.first_num + 10


class UserClass:
    num = Number()

    def __init__(self, num1: int, num2: int, values: list):
        self.num1 = num1
        self.num2 = num2
        self.values = values


    def __getattribute__(self, item):
        if item == 'num2':
            raise ValueError("Access is denied")
        else:
            return object.__getattribute__(self, item)


    def __getattr__(self, item):
        print(f"Uncknown attribute '{item}'")


    def __getitem__(self, item: int):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError("Incorrect index")


    @property
    def first_num(self):
        return self.num1


if __name__ == '__main__':
    user = UserClass(5, 6, [1, 2, 3, 4, 5])
    print(user.num)
    print(user.num1)
    print(user.values[3])
    print(user.num2)
