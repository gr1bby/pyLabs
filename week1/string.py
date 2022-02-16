def make_string(list_of_letters: list):
    try:
        sorted_list = sorted(list_of_letters)
        new_list = list()
        for index, letter in sorted_list:
            new_list.append(letter)
        return ''.join(new_list)
    except TypeError:
        return False


if __name__ == '__main__':
    list_of_tuples = [(4,'y'),(1,'o'),(3,'t'),(0,'m'),(2,'n')]
    print(make_string(list_of_tuples))
