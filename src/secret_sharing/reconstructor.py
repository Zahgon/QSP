from typing import List, Tuple
from .gf256 import gf_mul, gf_div


class SecretReconstructor:
    @classmethod
    def reconstruct(cls, shares: List[Tuple[int, bytes]]) -> bytes:
        pass
