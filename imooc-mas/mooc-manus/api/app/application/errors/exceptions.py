#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/04 0004 8:05
@Author : 756131502@qq.com
@File   : exceptions.py
"""
from typing import Any


class AppException(Exception):
    """基础应用异常类，继承RuntimeError"""

    def __init__(
            self,
            code: int = 400,  # 自定义业务错误码
            status_code: int = 400,
            msg: str = "应用发生错误，请稍后重试或联系管理员处理",
            data: Any = None
    ):
        """构造函数，完成错误数据初始化"""
        self.code = code
        self.status_code = status_code
        self.msg = msg
        self.data = data
        super().__init__()


class BadRequestError(AppException):
    """客户端请求错误"""

    def __init__(self, msg: str = "客户端请求参数错误"):
        super().__init__(status_code=400, code=400, msg=msg)


class NotFoundError(AppException):
    """资源不存在"""

    def __init__(self, msg: str = "资源不存在"):
        super().__init__(status_code=404, code=404, msg=msg)


class ValidationError(AppException):
    """验证错误"""

    def __init__(self, msg: str = "请求参数校验错误"):
        super().__init__(status_code=422, code=422, msg=msg)


class TooManyRequestsError(AppException):
    """请求频率过高"""

    def __init__(self, msg: str = "请求频率过高，请稍后重试"):
        super().__init__(status_code=429, code=429, msg=msg)


class ServerError(AppException):
    """服务器错误"""

    def __init__(self, msg: str = "服务器出现异常，请稍后重试或联系管理员处理"):
        super().__init__(status_code=500, code=500, msg=msg)
