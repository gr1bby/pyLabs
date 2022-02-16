def rank(height_in_rank: list, height: int) -> int:
    for one in height_in_rank:
        if height > one:
            return height_in_rank.index(one) + 1


if __name__ == '__main__':
    print(rank([165, 163, 160, 160, 157, 157, 155, 154], 160))