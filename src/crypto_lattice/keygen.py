import os
from .wrapper import LatticeWrapper

class KeyGen:
    
    @staticmethod
    def generate_keys() -> tuple[bytes, bytes]:
        pass

    @staticmethod
    def save_keys(pk: bytes, sk: bytes, pub_path: str, priv_path: str):
        pass

    @staticmethod
    def load_keys(pub_path: str, priv_path: str) -> tuple[bytes, bytes]:
        pass
