# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: scheduler_base.py
# @Author: Hung
# @Time: 2023/2/24 8:14
import importlib
from apscheduler.schedulers.tornado import TornadoScheduler


class CScheduler:
    client = None
    taskDict = {}
    # TODO 多进程只在一个进程注册

    @classmethod
    def init(cls):
        cls.client = TornadoScheduler()
        cls.add_jobs()
        cls.client.start()

    @classmethod
    def add_jobs(cls):
        for taskPath, taskCron in cls.taskDict.items():
            sTaskSubPath, sTaskMod = taskPath.rsplit(".", maxsplit=1)
            modObj = importlib.import_module(sTaskSubPath)
            cls.client(getattr(modObj, sTaskMod), "cron", **taskCron)

