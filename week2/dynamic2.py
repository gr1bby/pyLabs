def pack(backpack_weight: int, count_of_items: int, weight: list, cost: list) -> list:
    cell = [[0 for _ in range(backpack_weight + 1)] for _ in range(count_of_items + 1)] 
    for i in range(count_of_items + 1):
        for w in range(backpack_weight + 1):
            if i == 0 or w == 0:
                cell[i][w] = 0
            elif weight[i - 1] <= w:
                oneway = cost[i - 1] + cell[i - 1][w - weight[i-1]]
                otherway = cell[i - 1][w]
                cell[i][w] = max(oneway, otherway) 
            else:
                cell[i][w] = cell[i - 1][w]

    matrix_for_return = list()
    for row in cell[1:]:
        matrix_for_return.append(row[1:])

    return matrix_for_return


if __name__ == '__main__':
    prices = [1500, 3000, 2000, 8000]
    weight = [1, 4, 3, 7]
    backpack_weight = 20
    max_price = 7000
    best_way = 0
    count_of_items = len(prices)

    backpack = pack( backpack_weight, count_of_items, weight, prices)
    for row in backpack:
        print(row)
    
    for row in backpack:
        for item in row:
            if item <= max_price and item >= best_way:
                best_way = item

    print(best_way)
