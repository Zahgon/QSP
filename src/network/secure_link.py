"""
src/network/secure_link.py
[Phase 8] 抗量子安全信道接管与可靠传输集成层 (注入心跳防老化机制)
将 Socket、加密通道、RUDP 队列、拥塞控制与 NAT 保活融为一体的终极门面。
"""

from typing import Callable, Optional
import time
import threading

from src.network.protocol import QSPProtocol, PacketType
from src.network.secure_channel import SecureChannel, ChannelState
from src.network.rudp import RUDPConnection
from src.network.congestion import HybridCongestionControl


class SecureLink:
    def __init__(self, 
                 send_raw_fn: Callable[[bytes, tuple], None], 
                 peer_addr: tuple, 
                 session_id: int, 
                 role: str = 'client', 
                 peer_fp: str = "",          # 改为接收指纹字符串
                 local_pk: bytes = b"",      # 新增传入本地公钥
                 local_sk: bytes = b""):
        
        print(f"[SecureLink] === 初始化安全链接 ===")
        print(f"[SecureLink] 对方地址: {peer_addr}")
        print(f"[SecureLink] 会话 ID: {session_id}")
        print(f"[SecureLink] 角色: {role}")
        
        self._send_raw_external = send_raw_fn
        self.peer_addr = peer_addr
        self.session_id = session_id

        # 实例化安全通道时传入指纹和公钥
        self.sec_channel = SecureChannel(role=role, my_pk=local_pk, my_sk=local_sk, peer_fp=peer_fp)
        self.rudp = RUDPConnection(session_id)
        self.cc = HybridCongestionControl()

        self.on_handshake_done: Optional[Callable] = None
        self.on_data_received: Optional[Callable[[bytes], None]] = None

        # --- NAT 洞口防老化心跳机制 ---
        self.last_send_time = time.time()
        self.last_recv_time = time.time()
        self.is_running = True
        self.heartbeat_interval = 15.0 # 每 15 秒空闲触发一次
        
        self.heartbeat_thread = threading.Thread(target=self._heartbeat_loop, daemon=True)
        self.heartbeat_thread.start()

    def stop(self):
        """安全释放后台心跳线程"""
        pass

    def _send_wrapped(self, data: bytes):
        """统一拦截发送操作，更新最后发送时间，压制冗余心跳"""
        pass

    def _heartbeat_loop(self):
        """心跳守护线程：侦测空闲状态并发送 KEEPALIVE 刷新路由器 NAT 映射"""
        pass

    def initiate_security_handshake(self):
        pass

    def handle_network_packet(self, parsed_pkt: dict):
        # 只要收到来自该通道的任何包，都更新接收时间
        pass

    def send_reliable(self, cleartext: bytes):
        pass
