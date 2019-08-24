#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : etc.py
# Create date : 2019-08-17 13:40
# Modified date : 2019-08-24 10:24
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

NEO4J_HOST = "192.168.4.105" # neo4j 搭载服务器的ip地址，ifconfig可获取到
NEO4J_PORT = "7474" # neo4j 服务器监听的端口号
NEO4J_USER = "neo4j" # 数据库user name，如果没有更改过，应该是neo4j
#NEO4J_PASSWORD = "password"
NEO4J_PASSWORD = ""

if NEO4J_PASSWORD == "":
    print("need to set NEO4J_PASSWORD in etc.py")

if NEO4J_USER == "":
    print("need to set NEO4J_USER in etc.py")
