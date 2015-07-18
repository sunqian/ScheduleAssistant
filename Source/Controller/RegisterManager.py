#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls
from Model import UserTable

def register(my_id, my_name, my_pass):
    result = UserTable.select(my_id, 0, 'id')
    
    if result:
        return 'Existed'
    
    if not result:
        UserTable.insert(my_id, my_name, my_pass)
            return 'RGSuccess'