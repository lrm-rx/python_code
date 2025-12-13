#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/12/13 0013 21:50
@Author : 756131502@qq.com
@File   : config.py
"""


class Config:
    def __init__(self):
        # 关闭wtf的csrf保护
        self.WTF_CSRF_ENABLED = False
