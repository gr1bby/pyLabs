from multiprocessing import Pool

from timer import Timer
from pi import find_pi


COUNT_OF_PROCESSES = 10
COUNT_OF_POINTS = 10000000


if __name__ == '__main__':
    timer = Timer()
    with timer:
        with Pool(processes=COUNT_OF_PROCESSES) as processes:
            all_pi_results = processes.imap(find_pi, [COUNT_OF_POINTS for _ in range(COUNT_OF_PROCESSES)])
            avg_pi = sum(all_pi_results) / COUNT_OF_PROCESSES
            print(avg_pi)

    print(timer.time)
