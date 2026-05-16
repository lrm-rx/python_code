#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/05/05 0005 11:38
@Author : 756131502@qq.com
@File   : app_config.py
"""
from pydantic import BaseModel, ConfigDict, HttpUrl, Field


class LLMConfig(BaseModel):
    """语言模型配置"""
    base_url: HttpUrl = "https://api.deepseek.com"
    api_key: str = ""
    model_name: str = "DeepSeek-V4-flash"
    temperature: float = Field(default=0.7)
    max_tokens: int = Field(8192, ge=0)


class AgentConfig(BaseModel):
    """Agent通用配置"""
    max_iterations: int = Field(default=100, gt=0, lt=1000)  # 最大迭代次数
    max_retries: int = Field(default=3, gt=1, lt=10)  # LLM/工具最大重试次数
    max_search_results: int = Field(default=10, gt=1, lt=100)  # 最大搜索结果数


class AppConfig(BaseModel):
    """应用配置信息, 包含Agent配置, LLM提供商, A2A网络, MCP服务配置等"""
    llm_config: LLMConfig  # 语言模型配置
    agent_config: AgentConfig  # Agent通用配置

    # Pydantic配置, 允许传递额外的字段初始化
    model_config = ConfigDict(extra="allow")
