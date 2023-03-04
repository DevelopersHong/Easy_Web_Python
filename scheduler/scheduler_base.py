# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: scheduler_base.py
# @Author: Hung
# @Time: 2023/2/24 8:14
import platform
import importlib
from apscheduler.schedulers.tornado import TornadoScheduler
from multiprocessing import Manager, Lock
from ctypes import c_bool

lock = Lock()
isRegister = Manager().Value(c_bool, False) if platform.system() != 'windows' else False


class CScheduler:
    client = None
    # 读取配置添加定时任务
    taskDict = {}

    # 多进程只在一个进程注册
    @classmethod
    def start(cls):
        with lock:
            if not isRegister.value:
                cls.init()
                isRegister.value = True

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

