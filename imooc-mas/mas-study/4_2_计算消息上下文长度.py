#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/03 0003 15:03
@Author : 756131502@qq.com
@File   : 4_2_计算消息上下文长度.py
"""
import transformers

# 创建分词器
tokenizer = transformers.AutoTokenizer.from_pretrained(
    "./resources/tokenizer",
    trust_remote_code=True
)

prompt = "你好，你是?"
messages = [{"role": "user", "content": "帮我计算下45243*123"}]

print("prompt: ", len(tokenizer.encode("你好，你是?")))
print("messages: ", len(tokenizer.apply_chat_template(messages)))
