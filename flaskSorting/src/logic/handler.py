from collections import defaultdict
from typing import Any, List

import api

from .sorting import *
from .timer import Timer
from .hashing import hash_list


timer = Timer()


def sort_data(data: List[Any], sort_method: str) -> List[Any] | str:
    seq = data.copy()

    match sort_method:
        case 'insertion':
            insertion_sort(seq)
        case 'merge':
            merge_sort(seq)
        case 'selection':
            selection_sort(seq)
        case 'quick':
            quick_sort(seq, 0, len(seq))
        case _:
            return 'unvailble sort_method'

    return seq


def handle(sort_method: str, value: List[Any]):
    data_list = defaultdict()
    data_for_db = defaultdict()
    with timer:
        data_for_db['unsorted'] = hashed_unsorted = hash_list(value)

        if api.db.find_by_hash(hashed_unsorted) is None:
            sorted_seq = sort_data(value, sort_method)
            data_list['sequence'] = data_for_db['sorted'] = sorted_seq
            api.db.insert_data(dict(data_for_db))
        else:
            data_list['sequence'] = api.db.find_by_hash(hashed_unsorted)[1:-1]

    data_list['time'] = timer.time
    return data_list


def get_sorted_answer(response: dict, sort_method: str) -> dict:
    for key, value in response.items():
        data_list = handle(sort_method, value)
        response[key] = data_list

    return response