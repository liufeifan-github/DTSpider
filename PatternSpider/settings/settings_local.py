#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
#
# @Time    : 2022/2/13 17:31
# @Author  : Feifan Liu
# @Email   : lff18731218157@163.com
# @File    : settings_local.py
# @Version : 1.0

# Copyright (C) 2022 北京盘拓数据科技有限公司 All Rights Reserved

# -*- coding: utf-8 -*-
import os, datetime

# =======================scrapy_配置=====================================================
ENV = 'local'  # 环境设置(本地，测试，线上)
BOT_NAME = 'PatternSpider'
SPIDER_MODULES = ['PatternSpider.spiders']
NEWSPIDER_MODULE = 'PatternSpider.spiders'
ROBOTSTXT_OBEY = False
DOWNLOAD_TIMEOUT = 60
COMMANDS_MODULE = 'PatternSpider.run'
CONCURRENT_REQUESTS = 16
REDIS_START_URLS_AS_SET_TAG = True
HTTPERROR_ALLOWED_CODES = [401, 400, 403]
IMAGES_STORE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

# ==================日志相关==========================================================================
today = datetime.datetime.now()
LOG_LEVEL = 'INFO'
LOG_FILE_TASK = "D:/logs/scrapy_redis/tasks/{}.log"

# ===scrapy_redis 读取的redis地址  task模块使用此连接地址，因为要保持一致=======================================
REDIS_URL = "redis://:@127.0.0.1:6379"
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWD = ''
REDIS_PARAMS = {'password': '', "decode_components": True}

# ==================中间件相关==========================================================================
DOWNLOADER_MIDDLEWARES = {
    'PatternSpider.middlewares.middlewares.RandomUserAgentMiddleware': 543,
    # 'PatternSpider.middlewares.middlewares.RandomProxyMiddleware': 600,
}
ITEM_PIPELINES = {
    'PatternSpider.pipelines.DownloadImagesPipeline': 1,
    'PatternSpider.pipelines.DataBasePipeline': 500,
}

# =========================selenium配置相关=========================================
CHROME_DIR = r"C:\Users\admin\AppData\Local\Google\Chrome\Application"

# ==================以下是不同实例数据库的连接信息==========================================================================
# mysql系列
MYSQL_BT_RESOURCE = {
    "host": '127.0.0.1',
    "port": 3306,
    "user": 'root',
    "pwd": '123456',
    "database": 'bt-resource',
}
MYSQL_DT = {
    "host": '127.0.0.1',
    "port": 3306,
    "user": 'root',
    "pwd": '123456',
    "database": 'social_data',
}

# mongo系列
MONGO_DT = {
    "host": '127.0.0.1',
    "port": 27017,
    "user": 'root',
    "pwd": '123456',
}
# redis系列
REDIS_BT_RESOURCE = {
    'host': '127.0.0.1',
    'port': 6379,
    'pwd': '',
    'database': 0,
}
# es系列
ES_BT_RESOURCE = {
    'hosts': '10.168.160.104',
    'port': '9200',
    'username': '',
    'password': '',
    'index': 'bt-resource',
    'doc_type': 'bt-resource',
}
# minio ak sk  启动服务的时候获取
MINIO_DVIDS = {
    'host': "127.0.0.1",
    'port': "9000",
    'ak': "minioadmin",
    'sk': "minioadmin",
}
