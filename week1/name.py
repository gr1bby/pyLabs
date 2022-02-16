def split_name(full_name: str) -> list:
    unsorted_list = full_name.split()
    return unsorted_list[:3]


def print_name(sorted_name: list) -> None:
    for el in sorted_name:
        print(el.lower().capitalize())


if __name__ == '__main__':
    name = 'веСелоВ АЛЕКСей АЛЕКсандРОВИЧ 3 КУрС'
    print_name(split_name(name))