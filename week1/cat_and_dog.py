import sys


def calculate(years: int) -> list:
    list_of_ages = [years]
    catYears, dogYears = 0, 0

    for year in range(years):
        if year == 0:
            catYears += 15
            dogYears += 15

        elif year == 1:
            catYears += 9
            dogYears += 9

        else:
            catYears += 4
            dogYears += 5

    list_of_ages.append(catYears)
    list_of_ages.append(dogYears)

    return list_of_ages


if __name__ == '__main__':
    try:
        humanYears = int(sys.argv[1])
        if humanYears < 1: raise ValueError
        list_of_ages = calculate(humanYears)
        print(list_of_ages)
    except ValueError: 
        print("Incorrect value")
