from timer import Timer


def selection_sort(nums: list) -> None:
    for i in range(0, len(nums) - 1):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]


if __name__ == '__main__':
    nums = [3, 17, 2, 16, 23, 4]
    t = Timer()
    t.start()
    selection_sort(nums)
    t.stop()
    print(nums)