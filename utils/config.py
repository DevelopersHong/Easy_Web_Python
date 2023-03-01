# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: config.py
# @Author: Hung
# @Time: 2023/2/25 21:03
import yaml
import codecs
from munch import Munch
from loguru import logger


class Config:

    @logger.catch()
    def init(self, config_path):
        with codecs.open(config_path, encoding='utf8') as r:
            self.m_ConfigInfo = Munch(yaml.load(r, Loader=yaml.FullLoader))

        self.m_ServerInfo = Munch(self.m_ConfigInfo.server)
        self.m_MysqlInfo = Munch(self.m_ConfigInfo.mysql)
        self.m_LogInfo = Munch(self.m_ConfigInfo.log)


class NewConfig:
    _confObj = None

    @classmethod
    def init(cls, config_path="./configuration/application.yml"):
        if not cls._confObj:
            cls._confObj = Config()
            cls._confObj.init(config_path)
        return cls._confObj


g_ConfigObj = NewConfig.init()
