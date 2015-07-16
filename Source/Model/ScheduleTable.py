#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'schedule'

def select(sid, sname, stype):
    if stype == 'id':
        schedules = db.select(tb, where='id="'+sid+'"')
        return schedules;

    elif stype == 'name':
        schedules = db.select(tb, where='s_name="'+sname+'"')
        return schedules

    elif stype == 'all':
        schedules = db.select(tb)
        return schedules

    elif stype == 'norder':
        schedules = db.select(tb, where='s_name="'+sname+'"', order='s_time asc')
        return schedules

    elif stype == 'order':
        schedules = db.select(tb, order='s_time asc')
        return schedules

#def insert(my_id, my_name, my_pass):
 #   db.insert(tb, s_id=my_id, s_name=my_name, s_pass=my_pass)


def update(sid , skeep):
    db.update(tb, where='id="'+sid+'"', keep=skeep)

def delete(sid, sname, stype):
    if stype == 'id':
        db.delete(tb, where='id=$sid', vars=locals())
    elif stype == 'name':
        db.delete(tb, where='s_name=$sname', vars=locals())

    
