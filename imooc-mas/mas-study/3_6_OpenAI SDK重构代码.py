#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/03 0003 9:53
@Author : 756131502@qq.com
@File   : 3_5_Kimi多模态API测试.py
"""
import os

import dotenv
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "你好，你是?"}]
)

print("推理内容:", response.choices[0].message.reasoning_content)
print("最终答案:", response.choices[0].message.content)
