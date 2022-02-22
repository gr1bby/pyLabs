def quicksort(alist: list, start: int, end: int) -> None:
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)
 
 
def partition(alist: list, start: int, end: int) -> int:
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
 
if __name__ == '__main__':
    alist = [5, 11, 5, 3, 0, 12, 9, 16, 3, 27, 4]
    quicksort(alist, 0, len(alist))
    print(alist)