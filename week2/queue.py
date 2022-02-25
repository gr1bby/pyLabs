from collections import deque


def queue_time(clients: list, n: int) -> int:
    assert n >= 1 and clients
    queue = deque(clients)
    total_time = 0
    workers = [0 for _ in range(n)]
    while True:
        for i in range(n):
            if workers[i] == 0:
                if queue:
                    workers[i] = queue.popleft()
            if workers[i] > 0:
                workers[i] -= 1
        if queue or any([w > 0 for w in workers]):
            total_time += 1
        else:
            return total_time + 1



if __name__ == '__main__':
    try: print(queue_time([], 1))
    except AssertionError: print('There are no customers or cashboxes')
    try: print(queue_time([5,5,4,4], 0))
    except AssertionError: print('There are no customers or cashboxes')
    try: print(queue_time([10,2,3,3], 2))
    except AssertionError: print('There are no customers or cashboxes')
    try: print(queue_time([2,3,10], 2))
    except AssertionError: print('There are no customers or cashboxes')
