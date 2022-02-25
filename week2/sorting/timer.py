import time


class TimeError(Exception):
    pass


class Timer:
    def __init__(self):
        self.start_time = None

    
    def start(self):
        if self.start_time is not None:
            raise TimeError("The timer is working. Use stop() to stop.")

        self.start_time = time.perf_counter()


    def stop(self):
        if self.start_time is None:
            raise TimeError("The timer is not working. Use start() to start.")

        elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None
        print(f"Calculation took {elapsed_time:0.10f} seconds")