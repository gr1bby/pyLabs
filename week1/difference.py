def findDif(firstDate: str, secondDate: str) -> int:
    # get year part and convert to int
    firstYear = int(firstDate.split('/')[0]) 
    secondYear = int(secondDate.split('/')[0])
    # find result and get absolute value
    return abs(firstYear - secondYear)


if __name__ == '__main__':
    print(findDif('2002/23/10', '2022/2/3'))
    print(findDif('2022/23/10', '2002/2/3'))
