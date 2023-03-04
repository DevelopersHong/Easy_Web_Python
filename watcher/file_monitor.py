# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: file_monitor.py
# @Author: Hung
# @Time: 2023/2/25 20:49
from watchdog.events import RegexMatchingEventHandler


class CFileWatchHandler(RegexMatchingEventHandler):
    def __init__(self):
        super(CFileWatchHandler, self).__init__()

    def on_modified(self, event):
        pass

    @staticmethod
    def rebuild_config():
        # 重新加载项目配置
        pass

    @staticmethod
    def rebuild_scheduler():
        # 重新注册定时任务
        pass
