"""
src/app/app_protocol.py
[Application Phase 1] 应用层传输协议定义
负责业务指令与二进制数据（如 Shamir 份额）的 JSON/Base64 序列化与反序列化。
"""

import json
import base64
from enum import Enum
from typing import Optional, Dict, Any


class AppCmd(str, Enum):
    """应用层核心指令集"""
    SHARE_PUSH = "SHARE_PUSH"
    PULL_REQ = "PULL_REQ"
    PULL_RESP = "PULL_RESP"
    ERROR = "ERROR"


class AppMessage:
    """
    应用层消息对象。
    统一封装各类业务请求，处理二进制 payload 的 Base64 自动转换。
    """
    def __init__(self, 
                 cmd: AppCmd, 
                 file_hash: str, 
                 share_index: Optional[int] = None, 
                 share_data: Optional[bytes] = None,
                 error_msg: Optional[str] = None,
                 chunk_index: int = 0,
                 total_chunks: int = 1):
        self.cmd = cmd
        self.file_hash = file_hash
        self.share_index = share_index
        self.share_data = share_data
        self.error_msg = error_msg
        self.chunk_index = chunk_index
        self.total_chunks = total_chunks

    def pack(self) -> bytes:
        pass

    @classmethod
    def unpack(cls, data: bytes) -> "AppMessage":
        pass
