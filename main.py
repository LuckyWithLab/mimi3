#!/usr/bin/env python3
"""
mimo2api 系统统一个化主入口

启动前只需修改此处的全局配置。
"""
import os
import sys
import logging
import uvicorn
from dotenv import load_dotenv

load_dotenv()

# ================= 统一全局配置（优先读 .env，有默认值兜底） =================
SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("SERVER_PORT", "8000"))
WS_TUNNEL_URL = os.getenv("WS_TUNNEL_URL", f"ws://your-domain.com:{SERVER_PORT}/ws")
# ================================================

os.environ["MIMO2API_WS_URL"] = WS_TUNNEL_URL

# 引入实际带 Lifespan 背景挂载服务的 FastAPI APP 对象
from mimo2api.web_service import app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info(f"🚀 mimo2api 统一主入口 - 正在启动网关并绑定集群到 {SERVER_HOST}:{SERVER_PORT}")
    logging.info(f"🔗 云端要求 Claw 主动连接的桥接 WS URL 将统一下发为: {WS_TUNNEL_URL}")
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT, ws_max_size=10**8)
