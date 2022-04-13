from hashlib import sha256
from typing import Any, List


def hash_list(seq: List[Any]) -> str:
    byte_seq = str(seq).encode()

    _hash = sha256(byte_seq)

    return _hash.hexdigest()