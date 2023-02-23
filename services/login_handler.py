# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: login_handler.py
# @Author: Hung
# @Time: 2023/2/23 23:05

from services.base import CMiddleHandler


class CLoginHandler(CMiddleHandler):
    def initialization(self):
        super(CLoginHandler, self).initialization()

    def post_handler(self):
        self.get_json()
        self.response_json()

