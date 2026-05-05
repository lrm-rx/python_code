#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/05 0005 11:56
@Author : 756131502@qq.com
@File   : app_config_repository.py
"""
from typing import Protocol, Optional

from app.domain.models.app_config import AppConfig


class AppConfigRepository(Protocol):
    """应用配置仓库"""

    def load(self) -> Optional[AppConfig]:
        """加载应用配置"""
        ...

    def save(self, app_config: AppConfig) -> None:
        """存储更新的应用配置"""
        ...
