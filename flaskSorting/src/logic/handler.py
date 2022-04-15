from collections import defaultdict
from typing import Any, List

import api

from .sorting import Sorting
from .timer import Timer
from .hashing import hash_list


timer = Timer()


def sort_data(data: List[Any], sort_method: str) -> List[Any] | str:
    seq = data.copy()

    methods = {
        sort_name: getattr(Sorting, sort_name) for sort_name in Sorting.__all__
    }

    if sort_method in methods.keys():
        methods[sort_method]
        return ','.join(map(str, seq))
    else:
        return 'unvailble sort method'


def handle(sort_method: str, value: List[Any]):
    data_list = defaultdict()
    data_for_db = defaultdict()

    with timer:
        data_for_db['unsorted'] = hashed_unsorted = hash_list(value)
        data_from_db = api.db.find_by_hash(hashed_unsorted)

        if data_from_db is None:
            sorted_seq = sort_data(value, sort_method)
            data_for_db['sorted'] = sorted_seq
            if ',' in sorted_seq:
                data_list['sequence'] = sorted_seq.split(',')
            else:
                data_list['sequence'] = sorted_seq
            api.db.insert_data(dict(data_for_db))
        else:
            if ',' in data_from_db:
                data_list['sequence'] = data_from_db.split(',')
            else:
                data_list['sequence'] = data_from_db

    data_list['time'] = timer.time
    return data_list


def get_sorted_answer(response: dict, sort_method: str) -> dict:
    for key, value in response.items():
        data_list = handle(sort_method, value)
        response[key] = data_list

    return response