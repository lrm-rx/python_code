#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/12/13 0013 21:41
@Author : 756131502@qq.com
@File   : app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天接口请求验证"""
    # 必填, 长度最大为2000
    query = StringField("query", validators=[
        DataRequired(message="用户的提问内容为必填项"),
        Length(max=2000, message="用户的提问内容最大长度是2000")
    ])
