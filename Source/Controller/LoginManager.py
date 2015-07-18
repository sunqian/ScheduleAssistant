#!/usr/bin/env python
# coding: utf-8
from Config import settings
from Config.url import urls
from Model import UserTable

render = settings.render
db = settings.db


def login(sid, pw):

     data = UserTable.select(sid, 0, 'id')
     user = []
     for i in data:
         user.append(i)
        
     if not user:
         return 'NotExist'

     if pw != user[0].s_pass:
         return 'PWFalse'

     else:
         return user[0].s_name
    
    
