#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'finalschedule'

def select(sid, stype):
    if stype == 'id':
        schedules = db.select(tb, where='id="'+sid+'"', vars=locals())
        return schedules;

    elif stype == 'all':
        schedules = db.select(tb)
        return schedules

    elif stype == 'order':
        schedules = db.select(tb, order='s_time asc')
        return schedules

def insert(sname, stime):
    db.insert(tb,  s_name=sname, s_time=stime)


def update(sid , schange, sperson, sfinish, stype):
    if stype == 'Fs':
        db.update(tb, where='id=$sid', finish=sfinish, vars=locals())

    elif stype == 'FsCh':
        db.update(tb, where='id=$sid', finish=sfinish, ischange=schange, vars=locals())

    elif stype == 'PFs':
        db.update(tb, where='id=$sid', person=sperson, finish=sfinish, vars=locals())

    elif stype == 'IsC':
        db.update(tb, where='id=$sid', ischange=schange, vars=locals())


def delete():
    db.delete(tb, where='id=finalschedule.id')

    
