#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'user_data'

def select(my_id, my_name, my_type):
    if my_type == 'id':
        users = db.select(tb, where='s_id=$my_id', vars=locals())
        return users;

    elif my_type == 'name':
        users = db.select(tb, where='s_name="'+my_name+'"')
        return users

    elif my_type == 'all':
        users = db.select(tb)
        return users

    elif my_type == 'order':
        users = db.select(tb, order='s_id asc')
        return users

def insert(my_id, my_name, my_pass):
    db.insert(tb, s_id=my_id, s_name=my_name, s_pass=my_pass)


def update(name , duty):
    db.update(tb, where='s_name="'+name+'"', time_duty=duty)

def delete(sid):
    db.delete(tb, where='s_id=$sid', vars=locals())

    
