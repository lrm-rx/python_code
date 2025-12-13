#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/12/07 0007 18:57
@Author : 756131502@qq.com
@File   : http.py
"""

from flask import Flask

from config import Config
from internal.router import Router


class Http(Flask):
    """ Http服务引擎 """

    def __init__(self, *args, conf: Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)

        self.config.from_object(conf)
