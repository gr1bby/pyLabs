import time

from typing import Optional, Type
from types import TracebackType


class Timer:
    def __init__(self):
        self.__calculated_time = None


    @property
    def time(self):
        return self.__calculated_time
           

    def __enter__(self):
        self.__calculated_time = None
        self.start_time = time.perf_counter()

    
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]):

        self.__calculated_time = time.perf_counter() - self.start_time
