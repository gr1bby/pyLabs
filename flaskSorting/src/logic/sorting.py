from typing import Any, List


__all__ = [
    'insertion_sort',
    'merge_sort',
    'selection_sort',
    'quick_sort',
]


def insertion_sort(list_of_nums: List[Any]):
    for i in range(1, len(list_of_nums)):
        item_to_insert = list_of_nums[i]
        j = i - 1
        while j >= 0 and list_of_nums[j] > item_to_insert:
            list_of_nums[j + 1] = list_of_nums[j]
            j -= 1
        list_of_nums[j + 1] = item_to_insert


def merge_sort(list_of_nums: List[Any]) -> None:
    if len(list_of_nums) > 1:
        middle = len(list_of_nums) // 2
        left_part = list_of_nums[:middle]
        right_part = list_of_nums[middle:]
        merge_sort(left_part)
        merge_sort(right_part)

        i = j = k = 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                list_of_nums[k] = left_part[i]
                i += 1
            else:
                list_of_nums[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            list_of_nums[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            list_of_nums[k] = right_part[j]
            j += 1
            k += 1


def selection_sort(nums: List[Any]):
    for i in range(0, len(nums) - 1):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]


def quick_sort(alist: List[Any], start: int, end: int):
    if end - start > 1:
        p = partition(alist, start, end)
        quick_sort(alist, start, p)
        quick_sort(alist, p + 1, end)


def partition(alist: List[Any], start: int, end: int) -> int:
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j
