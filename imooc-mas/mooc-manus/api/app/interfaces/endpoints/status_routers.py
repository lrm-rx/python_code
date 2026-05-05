#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/03 0003 22:07
@Author : 756131502@qq.com
@File   : status_routers.py
"""
import logging
from typing import List

from fastapi import APIRouter, Depends

from app.application.services.status_service import StatusService
from app.domain.models.health_status import HealthStatus
from app.interfaces.schemas import Response
from app.interfaces.service_dependencies import get_status_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/status", tags=["状态模块"])


@router.get(
    path="",
    response_model=Response[List[HealthStatus]],
    summary="系统健康检查",
    description="检查系统的运行状态，返回系统状态信息"
)
async def get_status(
        status_service: StatusService = Depends(get_status_service),
) -> Response:
    """获取系统状态"""
    status_list = await status_service.check_all()

    if any(item.status == "error" for item in status_list):
        return Response.fail(503, "系统存在服务异常", status_list)
    return Response.success(msg="系统健康检查成功", data=status_list)
