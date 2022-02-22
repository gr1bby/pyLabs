def get_count_of_ways(amount: int, coins: list) -> int:
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    if len(coins) == 1:
        return amount % coins[0] == 0
    return get_count_of_ways(amount - coins[0], coins) + get_count_of_ways(amount, coins[1:])
 

if __name__ == '__main__':
    coins = [1, 2, 5, 10]
    amount = 10
    print(get_count_of_ways(amount, coins))
