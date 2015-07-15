#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls
from Model import UserTable
from Model import FinalUserTable
from Model import ScheduleTable
from Model import FinalScheduleTable

render = settings.render
db = settings.db
tb = 'schedule'

def attend(sid):

    schedule = FinalScheduleTable.select(sid, 'id')
    name = schedule[0].s_name
    user = FinalUserTable.select(name, 'name')
    actual = user[0].time_actual + 1

    FinalUserTable.update(name, actual, 'Vars')
    FinalScheduleTable.update(sid, 0, 0, '1', 'Fs')

def undo(sid):

    schedule = FinalScheduleTable.select(sid, 'id')
    myschedule = schedule[0]
    change = myschedule.ischange
    if not change:
        name = myschedule.s_name
    else:
        name = myschedule.person
    

    user = FinalUserTable.select(name, 'name')
    actual = user[0].time_actual - 1
    FinalUserTable.update(name, actual, 'Vars')
    FinalScheduleTable.update(sid, '0', 0, '0', 'FsCh')

def cover(sid):
    FinalScheduleTable.update(sid, '1', 0, 0, 'IsC')

def coverUndo(sid):
    FinalScheduleTable.update(sid, '0', 0, 0, 'IsC')

def coverPerson(sid):
    myperson = web.input().get('person')

    result = FinalUserTable.select(myperson, 'name')
    if not result:
        return False

    FinalScheduleTable.update(sid, 0, myperson, '1', 'PFs')
    schedule = FinalScheduleTable.select(sid, 'id')
    user = FinalUserTable.select(myperson, 'name')
    actual = user[0].time_actual + 1
    FinalUserTable.update(myperson, actual, 'Vars')

    return True
