def get_ways(amount: int, coins: list, lastindex=0, lst=[]) -> None:
    if amount == 0:
        print(lst)
    else:
        for i in range(lastindex, len(coins)):
            if coins[i] <= amount:
                get_ways(amount - coins[i], coins, i, lst + [coins[i]])


if __name__ == '__main__':
    amount = 10
    coins = [1, 2, 5]
    get_ways(amount, coins)
