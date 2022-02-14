from math import ceil


def movie(card: int, ticket: int, perc: float) -> int:
    times = 0
    sys_a, sys_b = 0, card
    while ceil(sys_b) > sys_a:
        times += 1
        sys_a += ticket
        sys_b += ticket*(perc**times)
    
    print(f"{times} times (with card the total price is {ceil(sys_b)}, with tickets {sys_a})")


if __name__ == '__main__':
    movie(100, 10, 0.95)
