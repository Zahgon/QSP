"""
src/app/app_router.py
[Application Phase 2] 业务消息路由与事件总线
负责将网络层的原始数据流反序列化，并线程安全地分发到各个业务逻辑处理器。
"""

import traceback
from typing import Callable, Dict, Optional, Tuple
from .app_protocol import AppMessage, AppCmd


class AppRouter:
    """
    应用层消息路由器。
    桥接异步后台网络事件与主线程业务逻辑。
    """
    def __init__(self, ui_invoker: Optional[Callable] = None):
        self.handlers: Dict[AppCmd, Callable[[Tuple[str, int], AppMessage], None]] = {}
        self.ui_invoker = ui_invoker

    def register_handler(self, cmd: AppCmd, handler: Callable[[Tuple[str, int], AppMessage], None]):
        pass

    def dispatch_network_data(self, peer_addr: Tuple[str, int], raw_data: bytes):
        pass
