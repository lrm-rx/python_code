#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/12/18 0018 22:16
@Author : 756131502@qq.com
@File   : conftest.py
"""

import pytest

from app.http.app import app


@pytest.fixture
def client():
    """获取Flask应用的测试应用, 并返回"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
