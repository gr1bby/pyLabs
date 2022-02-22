def selection_sort(nums: list) -> None:
    for i in range(0, len(nums) - 1):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]


if __name__ == '__main__':
    nums = [5, 3, 6, 18, 19, 2]
    selection_sort(nums)
    print(nums)