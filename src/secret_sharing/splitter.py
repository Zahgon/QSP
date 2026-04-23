import os
from typing import List, Tuple
from .gf256 import gf_mul


class SecretSplitter:
    @classmethod
    def split_secret(cls, secret: bytes, t: int, n: int) -> List[Tuple[int, bytes]]:
        # 使用 bytearray 矩阵化操作，避免频繁创建字节串
        pass
