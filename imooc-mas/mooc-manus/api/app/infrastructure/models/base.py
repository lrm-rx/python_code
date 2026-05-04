#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/04 0004 13:55
@Author : 756131502@qq.com
@File   : base.py
"""
from sqlalchemy.orm import declarative_base

# 定义基础ORM类，让所有模型都继承这个类
Base = declarative_base()
