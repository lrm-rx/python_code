#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/12/19 0019 22:22
@Author : 756131502@qq.com
@File   : module.py
"""
from flask_sqlalchemy import SQLAlchemy
from injector import Binder
from injector import Module

from internal.extension.database_extension import db


class ExtensionModule(Module):
    # 扩展模块的依赖注入
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
