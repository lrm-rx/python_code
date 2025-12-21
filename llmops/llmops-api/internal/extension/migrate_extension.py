#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/12/21 0021 12:42
@Author : 756131502@qq.com
@File   : migrate_extension.py
"""

from flask_migrate import Migrate

migrate = Migrate()

# flask --app app.http.app db init
# flask --app app.http.app db migrate -m "create_table"
