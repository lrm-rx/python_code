#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/04 0004 7:51
@Author : 756131502@qq.com
@File   : exception_handlers.py
"""
import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

from app.application.errors.exceptions import AppException
from app.interfaces.schemas import Response

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI):
    """处理项目中所有的异常并进行统一处理，涵盖：自定义业务状态异常、HTTP异常、通用异常"""

    @app.exception_handler(AppException)
    async def app_exception_handler(req: Request, e: AppException) -> JSONResponse:
        """处理自定义业务状态异常"""
        logger.error(f"AppException: {str(e.msg)}")
        return JSONResponse(
            status_code=e.status_code,
            content=Response(
                code=e.code,
                msg=e.msg,
                data={}
            ).model_dump()
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(req: Request, e: HTTPException) -> JSONResponse:
        """处理FastAPI抛出的HTTP异常"""
        logger.error(f"HTTPException: {str(e.detail)}")
        return JSONResponse(
            status_code=e.status_code,
            content=Response(
                code=e.status_code,
                msg=str(e.detail),
                data={}
            ).model_dump()
        )

    @app.exception_handler(Exception)
    async def exception_handler(req: Request, e: Exception):
        """处理抛出的未定义的任意异常，将状态码统一设置为500"""
        logger.error(f"Exception: {str(e)}")
        return JSONResponse(
            status_code=500,
            content=Response(
                code=500,
                msg="服务器出现异常，请稍后重试或联系管理员处理"
            ).model_dump()
        )
