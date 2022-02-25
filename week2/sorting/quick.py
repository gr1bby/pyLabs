from sqlite3 import Time
from timer import Timer


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
    alist = [3, 17, 2, 16, 23, 4]
    t = Timer()
    t.start()
    quicksort(alist, 0, len(alist))
    t.stop()
    print(alist)