#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/03 0003 22:07
@Author : 756131502@qq.com
@File   : status_routers.py
"""
import logging

from fastapi import APIRouter

from app.interfaces.schemas import Response

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/status", tags=["状态模块"])


@router.get(
    path="",
    response_model=Response,
    summary="系统健康检查",
    description="检查系统的运行状态，返回系统状态信息"
)
async def get_status() -> Response:
    """获取系统状态"""
    return Response.success()
