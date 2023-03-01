# -*- coding: utf-8 -*-
# @Project: Easy_Web_Python
# @File: main.py
# @Author: Hung
# @Time: 2023/2/23 8:29

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from loguru import logger
from datetime import datetime

from services.login_handler import CLoginHandler
from scheduler.scheduler_base import CScheduler
from watcher.watch_base import CWatcher
from utils.config import g_ConfigObj


tornado.options.define("env", default="dev", type=str)
tornado.options.parse_command_line()


def main():
    # 启动日志
    file_name = datetime.now().strftime("%Y%m")
    logger.add(f"{g_ConfigObj.m_LogInfo.path}/{file_name}.log", level=g_ConfigObj.m_LogInfo.level)
    logger.info(f"Starting Server")
    # 注册路由
    handlerList = [
        (r"/login", CLoginHandler)
    ]
    application = tornado.web.Application(handlerList)
    # 初始化中间件

    # 注册定时任务
    CScheduler.start()
    # 注册监控
    CWatcher.init()
    # 服务启动
    server = tornado.httpserver.HTTPServer(application)
    server.bind(8080)
    server.start(0)  # Forks multiple sub-processes
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()