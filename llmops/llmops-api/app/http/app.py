#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/12/07 0007 19:02
@Author : 756131502@qq.com
@File   : app.py
"""
import dotenv
from flask_sqlalchemy import SQLAlchemy
from injector import Injector

from config import Config
from internal.router import Router
from internal.server import Http
from .module import ExtensionModule

# 将env加载到环境变量中
dotenv.load_dotenv()
injector = Injector([ExtensionModule])
conf = Config()

app = Http(__name__, conf=conf, db=injector.get(SQLAlchemy), router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
