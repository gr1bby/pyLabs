from multiprocessing import Pool

from timer import Timer
from pi import find_pi


COUNT_OF_PROCESSES = 5
COUNT_OF_POINTS = 1000000


if __name__ == '__main__':
    timer = Timer()
    with timer:
        processes = Pool(processes=COUNT_OF_PROCESSES)
        all_pi_results = processes.map(find_pi, [COUNT_OF_POINTS for _ in range(COUNT_OF_PROCESSES)])
        processes.close()
        print(all_pi_results)

        avg_pi = sum(all_pi_results) / COUNT_OF_PROCESSES
        print(avg_pi)

    print(timer.time)
