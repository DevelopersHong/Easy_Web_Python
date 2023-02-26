# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: log_middleware.py
# @Author: Hung
# @Time: 2023/2/25 21:03

from middlewares.base import CMiddleWareBase


class CLogMiddleWare(CMiddleWareBase):
    @staticmethod
    def process_request():
        pass

    @staticmethod
    def process_response(self):
        pass
