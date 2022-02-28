import time


class Timer:
    def __init__(self):
        self.__calculated_time = None


    def get_time(self):
        if self.__calculated_time is not None:
            return self.__calculated_time
        else:
            return "Not calculated"            


    def __enter__(self):
        self.__calculated_time = None
        self.start_time = time.perf_counter()

    
    def __exit__(self, *exc_details):
        self.__calculated_time = time.perf_counter() - self.start_time


def just_func():
    l = list()
    for i in range(100000):
        l.append(i)


if __name__ == '__main__':
    timer = Timer()
    with timer:
        just_func()
    print(timer.get_time())
    