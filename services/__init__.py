# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: __init__.py
# @Author: Hung
# @Time: 2023/2/23 23:23
import tornado.web
import tornado.options


class CApplication(tornado.web.Application):
    def route(self, url):
        def register(handler):
            self.add_handler(".*$", [(url, handler)])
            return handler

        return register


def new_application():
    application = CApplication()
    tornado.options.define("app", default=application, type=tornado.web.Application)
    return application
