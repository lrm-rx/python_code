#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/12/18 0018 19:27
@Author : 756131502@qq.com
@File   : test_app_handler.py
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:
    """app控制器的测试类"""

    @pytest.mark.parametrize("query", [None, "你好, 你是谁?"])
    def test_completion(self, query, client):
        """
        # resp = client.post("/app/completion", json={"query": "你好, 你是?"})
        resp = client.post("/app/completion", json={"query": None})
        assert resp.status_code == 200
        # assert resp.json.get("code") == HttpCode.SUCCESS
        assert resp.json.get("code") == HttpCode.VALIDATE_ERROR
        # pytest -s -v 这个命令可以查看详情内容
        print("响应内容:", resp.json)
        """

        resp = client.post("/app/completion", json={"query": query})
        assert resp.status_code == 200
        if query is None:
            assert resp.json.get("code") == HttpCode.VALIDATE_ERROR
        else:
            assert resp.json.get("code") == HttpCode.SUCCESS
        # print("响应内容:", resp.json)
