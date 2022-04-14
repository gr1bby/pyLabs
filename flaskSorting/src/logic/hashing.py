from xxhash import xxh3_64_hexdigest
from typing import Any, List


def hash_list(seq: List[Any]) -> str:
    byte_seq = str(seq).encode()

    _hash = xxh3_64_hexdigest(byte_seq)

    return _hash