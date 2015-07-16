#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'finaluser_data'

def select(name, my_type):

    if my_type == 'name':
        users = db.select(tb, where='s_name=$name', vars=locals())
        return users

    elif my_type == 'all':
        users = db.select(tb)
        return users

    elif my_type == 'order':
        users = db.select(tb, order='s_name asc')
        return users

def insert(name, duty):
    db.insert(tb, s_name=name, time_duty=duty)


def update(name , tactual, my_type):
    if my_type == 'Vars':
        db.update(tb, where='s_name=$name', time_actual=tactual, vars=locals())

    elif my_type == 'Nov':
        db.update(tb, where='s_name="'+name+'"', time_actual=tactual)



def delete(name):
    db.delete(tb, where='s_name=$name', vars=locals())

    
