#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/03 0003 15:20
@Author : 756131502@qq.com
@File   : 4_4_ReAct+CoT实现企业业务表单填写.py
"""
import time


def make_coffee(customer: str) -> None:
    print(f"开始为 {customer} 煮咖啡...")
    time.sleep(5)  # 模拟耗时的I/O操作，例如:LLM请求调用获取结果
    print(f"{customer} 的咖啡好了")


def main_sync():
    start_time = time.time()
    make_coffee("顾客A")
    make_coffee("顾客B")
    make_coffee("顾客C")
    make_coffee("顾客D")
    make_coffee("顾客E")
    make_coffee("顾客F")
    end_time = time.time()
    print(f"同步方式总耗时: {end_time - start_time:.2f}秒")


if __name__ == "__main__":
    main_sync()
