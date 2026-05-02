#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/02 0002 23:01
@Author : 756131502@qq.com
@File   : 3_3_DeepSeek API调用.py
"""
import os

import dotenv
import requests
dotenv.load_dotenv()

with requests.request(
    "POST",
    "https://api.deepseek.com/v1/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
    },
    json={
        "model": "deepseek-v4-pro",
        "messages": [
            {"role": "user", "content": "你好，你是？"}
        ],
        "stream": True,
    },
) as response:
    for line in response.iter_lines(decode_unicode=True):
        if line:
            if line.startswith("data:"):
                data = line.lstrip("data:").strip()
                print("data:", data)


