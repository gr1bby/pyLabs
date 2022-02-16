def find_city(cities: str) -> list:
    main_cities = [
        'гродно', 'брест', 'витебск', 'могилев', 'гомель', 'минск', 
    ]
    sorted_list = list()

    words_for_sort = cities.split()
    for word in words_for_sort:
        if word.lower() in main_cities:
            sorted_list.append(word)

    return sorted_list


if __name__ == '__main__':
    print(find_city('привет грОдно ВитЕбск пока минСк'))
