#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/16 0016 16:39
@Author : 756131502@qq.com
@File   : uow.py
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Any

T = TypeVar("T", bound="IUnitOfWork")


class IUnitOfWork(ABC):
    """Uow模式协议接口"""
    file: Any
    session: Any

    @abstractmethod
    async def commit(self):
        """提交数据库数据持久化"""
        ...

    @abstractmethod
    async def rollback(self):
        """数据库回滚"""
        ...

    @abstractmethod
    async def __aenter__(self: T) -> T:
        """进入上下文管理器"""
        ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """退出上下文管理器"""
        ...
