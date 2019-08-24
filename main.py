#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-19 17:44
# Modified date : 2019-08-24 09:44
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from collect_info import GoodSchema

from build_kg import GoodsKg

def get_goods_list():
    handler = GoodSchema()
    handler.home_list()

def build_graph():
    handler = GoodsKg()
    handler.create_graph()

def run():
    #get_goods_list()
    build_graph()

run()
