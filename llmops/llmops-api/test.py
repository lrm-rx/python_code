#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/12/07 0007 18:20
@Author : 756131502@qq.com
@File   : test.py
"""

# python依赖注入demo

from injector import Injector, inject


class A:
    name: str = "lucky"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Class A的name:{self.a.name}")


injector = Injector()
# injector.binder.bind(A, to=A)  # 告诉注入器如何创建 A 的实例
b = injector.get(B)
b.print()
