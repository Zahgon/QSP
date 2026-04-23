"""
src/network/rudp.py
[Phase 3 Refactor] 可靠 UDP 传输核心引擎
彻底移除冗余的 RUDPSocket 包装，仅保留 SACK 滑动窗口与快速重传逻辑，交由 SecureLink 统一调度。
"""

import time
import threading
from typing import Dict, List, Tuple

class RUDPConnection:
    """
    维护单个 P2P 节点的可靠传输上下文（滑动窗口与 SACK 状态机）
    """
    def __init__(self, session_id: int):
        self.session_id = session_id
        
        self.next_seq_num = 1
        self.send_base = 1
        self.unacked_packets: Dict[int, dict] = {}
        self.lock = threading.RLock()
        
        self.rcv_base = 1
        self.out_of_order_buffer: Dict[int, bytes] = {}

    def receive_data(self, seq: int, payload: bytes) -> Tuple[List[bytes], int, List[Tuple[int, int]]]:
        pass

    def _calculate_sack_blocks(self) -> List[Tuple[int, int]]:
        pass

    def track_sent_packet(self, seq: int, payload: bytes):
        pass

    def handle_sack(self, ack: int, sack_blocks: List[Tuple[int, int]]) -> Tuple[List[Tuple[int, bytes]], float]:
        pass
