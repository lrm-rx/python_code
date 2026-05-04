#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/04 0004 16:50
@Author : 756131502@qq.com
@File   : conftest.py
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def client() -> TestClient:
    """
    创建一个可供所有测试用例使用的 TestClient 客户端。
    scope="session" 表示这个fixture 在整个测试用例只会实例一次，这样可以提高效率
    :return: TestClient
    """
    with TestClient(app) as c:
        yield c
