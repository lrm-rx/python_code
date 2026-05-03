#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/03 0003 15:20
@Author : 756131502@qq.com
@File   : 4_4_ReAct+CoT实现企业业务表单填写.py
"""
from typing import Union

from fastapi import FastAPI

# 1. 创建一个FastAPI实例
#    这个app对象就是我们所有API交互的核心
app = FastAPI()


# 2. 创建一个“路径操作” (Path Operation)
#    @app.get("/") 是一个“装饰器”，它告诉FastAPI：
#    当有HTTP GET请求访问根路径("/")时，
#    就执行下面的函数 root()
@app.get("/")
async def root():
    return {"message": "Hello, MoocManus!慕课网"}


# 3. 路径参数 (Path Parameters)
#    路径中的 {app_id} 会被作为参数传入函数
@app.get("/apps/{app_id}")
async def get_app(app_id: int, q: Union[str, None] = None):
    return {"app_id": app_id, "q": q}
