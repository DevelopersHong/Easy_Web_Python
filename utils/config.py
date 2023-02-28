# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: config.py
# @Author: Hung
# @Time: 2023/2/25 21:03
import yaml
import codecs


class Config:
    m_ConfigInfo = None

    @classmethod
    def init(cls, config_path="./configuration/application.yml"):
        with codecs.open(config_path, encoding='utf8') as r:
            cls.m_ConfigInfo = yaml.load(r, Loader=yaml.FullLoader)
        return cls.m_ConfigInfo


g_ConfigInfo = Config.init()

