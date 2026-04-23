import os
import json
import hashlib
import time
from typing import Optional

from src.app.app_protocol import AppMessage, AppCmd
from src.secret_sharing.splitter import SecretSplitter
from src.app.vault_crypto import VaultCrypto

class BackupManager:
    CHUNK_SIZE = 512
    ENCRYPTED_CHUNK_SIZE = 540  # 512 + 12(Nonce) + 16(Tag)

    def __init__(self, p2p_node, vault_password: str = "default_secure_password", vault_dir: str = "./data/shares"):
        self.p2p_node = p2p_node
        self.vault_dir = vault_dir
        if not os.path.exists(self.vault_dir):
            os.makedirs(self.vault_dir)
            
        self.vault_crypto = VaultCrypto(vault_password, self.vault_dir)

    def execute_backup(self, filepath: str, n: int, t: int) -> str:
        pass

    def _save_share_locally(self, file_hash: str, index: int, data: bytes):
        pass

    def handle_incoming_share(self, peer_addr: tuple, msg: AppMessage):
        pass
