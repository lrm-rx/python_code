#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time   : 2026/06/14 2026/06/14 星期日 23:18
@Author : 756131502@qq.com
@File   : supervisor.py
"""
from typing import Optional

from pydantic import BaseModel, Field


class TimeoutRequest(BaseModel):
    """激活超时销毁请求"""
    minutes: Optional[int] = Field(default=None, description="分钟数")
