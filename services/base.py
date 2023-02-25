# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: base.py
# @Author: Hung
# @Time: 2023/2/23 23:05
import importlib
from typing import Optional, Awaitable

import tornado.web


class CBaseHandler(tornado.web.RequestHandler):
    def initialization(self):
        pass

    async def post(self):
        pass

    async def post_handler(self):
        raise NotImplementedError

    async def get_json(self):
        pass

    async def response_json(self):
        pass


class CMiddleHandler(CBaseHandler):
    def initialization(self):
        super().initialization()
        self.m_MiddleWare = []

    async def prepare(self):
        await super().prepare()
        for sMiddleWare in self.m_MiddleWare:
            sMiddlePath, sMiddleMod = sMiddleWare.rsplit(".", maxsplit=1)
            modObj = importlib.import_module(sMiddlePath)
            await getattr(modObj, sMiddleMod).process_request(self, self.request)

    async def finish(self, chunk=None):
        for sMiddleWare in self.m_MiddleWare:
            sMiddlePath, sMiddleMod = sMiddleWare.rsplit(".", maxsplit=1)
            modObj = importlib.import_module(sMiddlePath)
            await getattr(modObj, sMiddleMod).process_reponse(self, self.request)
        await super().finish()
