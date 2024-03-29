from sqlite3 import Time
from timer import Timer


def merge_sort(list_of_nums: list) -> None:
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


if __name__ == '__main__':
    nums = [3, 17, 2, 16, 23, 4]
    t = Timer()
    t.start()
    merge_sort(nums)
    t.stop()
    print(nums)