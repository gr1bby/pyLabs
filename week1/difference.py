def find_dif(first_date: str, second_date: str) -> int:
    # get year part and convert to int
    first_year = int(first_date.split('/')[0]) 
    second_year = int(second_date.split('/')[0])
    # find result and get absolute value
    return abs(first_year - second_year)


if __name__ == '__main__':
    print(find_dif('2002/23/10', '2022/2/3'))
    print(find_dif('2022/23/10', '2002/2/3'))
