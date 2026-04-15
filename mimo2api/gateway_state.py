import asyncio
from typing import Dict, List
from fastapi import WebSocket

class GatewayState:
    def __init__(self):
        self.active_clients: List[WebSocket] = []
        self.pending_queues: Dict[str, asyncio.Queue] = {}
        self.current_client_index: int = 0

state = GatewayState()
