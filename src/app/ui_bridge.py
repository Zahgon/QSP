"""
src/app/ui_bridge.py
[Application Phase 5] UI 状态同步与线程安全保护
提供跨线程的安全 UI 更新机制，防止后台网络线程直接修改界面导致程序崩溃死锁。
"""

import threading
from tkinter import messagebox
from typing import Optional, Callable, Any


class UIBridge:
    def __init__(self, root):
        self.root = root
        
        self.lbl_net_status: Any = None
        self.progress_bar: Any = None
        self.btn_backup: Any = None
        self.btn_recovery: Any = None

    def bind_widgets(self, lbl_net_status, progress_bar, btn_backup, btn_recovery):
        pass

    def run_in_main_thread(self, func: Callable, *args, **kwargs):
        pass

    def safe_update_net_status(self, text: str, text_color: str = "white"):
        pass

    def safe_update_progress(self, current: int, total: int):
        pass

    def safe_show_info(self, title: str, message: str):
        pass

    def safe_show_error(self, title: str, message: str):
        pass

    def safe_set_action_buttons_state(self, state: str):
        pass
