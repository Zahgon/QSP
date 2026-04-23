"""
src/network/protocol.py
[Phase 8] RUDP 协议头与多路复用设计优化 (增加心跳保活)
包含协议类型定义、高精度时间戳封装与可变长 SACK 解析
"""

import struct
import time
from enum import IntEnum
from typing import List, Tuple, Optional, Dict, Any


class PacketType(IntEnum):
    # --- NAT 穿透与维持信令 ---
    HOLEPUNCH = 0x01
    HOLEPUNCH_ACK = 0x02
    KEEPALIVE = 0x03      # <--- 新增：心跳保活探测包
    
    # --- 抗量子安全握手 ---
    HANDSHAKE_INIT = 0x10
    HANDSHAKE_RESP = 0x11
    
    # --- 高带宽可靠传输 (RUDP) ---
    DATA = 0x20
    ACK = 0x21
    SACK = 0x22
    FIN = 0x2F


class QSPProtocol:
    MAGIC = 0x5153
    VERSION = 0x01
    HEADER_FORMAT = "!H B B I I I Q H"
    HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

    @classmethod
    def pack(cls, pkt_type: PacketType, seq: int, payload: bytes, ack: int = 0, session_id: int = 0, timestamp: Optional[int] = None) -> bytes:
        pass

    @classmethod
    def unpack(cls, data: bytes) -> Dict[str, Any]:
        pass

    @classmethod
    def build_sack_payload(cls, sack_blocks: List[Tuple[int, int]]) -> bytes:
        pass

    @classmethod
    def parse_sack_blocks(cls, payload: bytes) -> List[Tuple[int, int]]:
        pass
