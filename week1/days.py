def how_much_is_left(current_day: str) -> None:
    all_days = {
        'понедельник': 5,
        'вторник': 4,
        'среда': 3,
        'четверг': 2,
        'пятница': 1,
        'суббота': 0,
        'воскресенье': 0,
    }

    if current_day.lower() in all_days:
        days_left = all_days[current_day.lower()]

        if days_left == 0:
            print("Выходные уже наступили!")
        else:
            print(f"До выходных {days_left} дней")
    else:
        print("Неизвестный день недели")



if __name__ == '__main__':
    day = input("Введите день недели: ")
    how_much_is_left(day)