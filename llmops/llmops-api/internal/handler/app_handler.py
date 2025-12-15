#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/12/07 0007 18:36
@Author : 756131502@qq.com
@File   : app_handler.py
"""
import os

from flask import request
from openai import OpenAI

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validate_error_json


class AppHandler:
    """ 应用控制器 """

    def completion(self):
        """聊天接口"""
        # 1. 提取从接口中获取的输入
        query = request.json.get("query")
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2. 构建openai客户端, 并发起请求
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE"),
        )
        # 3. 得到请求响应, 然后将openai的响应传递给前端
        completion = client.chat.completions.create(
            model="kimi-k2-turbo-preview",
            messages=[
                {"role": "system",
                 "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
                {"role": "user", "content": query}
            ],
            temperature=0.6,
        )
        content = completion.choices[0].message.content

        # resp = Response(code=HttpCode.SUCCESS, message="", data={"content": content})

        return success_json({"content": content})

    def ping(self):
        raise FailException("数据没有找到")
        # return {"ping": "pink"}
