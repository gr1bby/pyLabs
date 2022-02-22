def insertion_sort(list_of_nums: list) -> None:
    for i in range(1, len(list_of_nums)):
        item_to_insert = list_of_nums[i]
        j = i - 1
        while j >= 0 and list_of_nums[j] > item_to_insert:
            list_of_nums[j + 1] = list_of_nums[j]
            j -= 1
        list_of_nums[j + 1] = item_to_insert


if __name__ == '__main__':
    list_of_nums = [3, 17, 2, 16, 23, 4]
    insertion_sort(list_of_nums)
    print(list_of_nums)