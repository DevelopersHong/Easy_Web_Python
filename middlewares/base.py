# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: base.py
# @Author: Hung
# @Time: 2023/2/25 21:02


class CMiddleWareBase:
    @staticmethod
    def process_request():
        raise NotImplementedError

    @staticmethod
    def process_response(self):
        raise NotImplementedError
