# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: watch_base.py
# @Author: Hung
# @Time: 2023/2/24 8:25
import atexit

from watchdog.observers import Observer

from watcher.file_monitor import CFileWatchHandler


class CWatcher:
    observer = None
    path = ""

    @classmethod
    def start_monitor(cls):
        cls.observer = Observer()
        cls.observer.schedule(CFileWatchHandler, cls.path)
        cls.observer.start()
        cls.observer.join()

    @classmethod
    def stop_monitor(cls):
        cls.observer.stop()

    @classmethod
    def init(cls):
        cls.start_monitor()
        atexit.register(cls.stop_monitor())
