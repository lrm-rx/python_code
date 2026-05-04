#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/03 0003 18:37
@Author : 756131502@qq.com
@File   : main.py
"""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.logging import setup_logging
from app.infrastructure.storage.redis import get_redis
from app.interfaces.endpoints.routes import router
from app.interfaces.errors.exception_handlers import register_exception_handlers
from core.config import get_settings

# 1. 加载配置信息
settings = get_settings()

# 2. 初始化日志系统
setup_logging()
logger = logging.getLogger()

# 3.定义FastAPI路由tags标签
openapi_tags = [
    {
        "name": "状态模块",
        "description": "包含**状态监测**等API接口，用于监测系统的运行状态"
    }
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    """创建FastAPI应用生命周期上下文管理器"""

    # 1.日志打印代码已经开始执行了
    logger.info("Eunoia正在初始化")

    # 2.初始化Redis缓存客户端
    redis = get_redis()
    await redis.init()

    try:
        # 3.lifespan分界点
        yield
    finally:
        # 4.应用关闭时执行
        await redis.shutdown()
        logger.info("Eunoia应用关闭成功")


# 4.创建MoocManus应用实例
app = FastAPI(
    title="Eunoia通用智能体",
    description="Eunoia是一个通用的AI Agent系统，可以完全私有部署，使用A2A+MCP连接Agent/Tool，同时支持在沙箱中运行各种内置工具和操作",
    lifespan=lifespan,
    openapi_tags=openapi_tags,
    version="1.0.0",
)

# 5.配置CORS中间件，解决跨域问题
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 6.注册异常处理函数
register_exception_handlers(app)

# 7.将路由添加到应用实例中
app.include_router(router, prefix="/api")
