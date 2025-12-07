#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/12/07 0007 18:40
@Author : 756131502@qq.com
@File   : router.py
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """ 路由 """
    app_handler: AppHandler

    # 以下构造函数因为使用了 dataclass, 所有可以不需要写
    # def __init__(self, app_handler: AppHandler):
    #     self.app_handler = app_handler

    def register_router(self, app: Flask):
        """ 注册路由 """

        # 1. 创建一个蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2. 将url与对应的控制器方法做绑定
        # app_handler = AppHandler()
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)

        # 3.在应用上去注册蓝图
        app.register_blueprint(bp)
