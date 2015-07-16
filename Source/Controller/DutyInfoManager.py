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

# get data
def data():

    user = UserTable.select(0, web.ctx.session.s_name, 'name')
    my_type = user[0].s_type

    if my_type == 0:
        schedules = ScheduleTable.select(0, web.ctx.session.s_name, 'norder')
        return (my_type, (schedules))

    elif my_type == 1:

        schedules = ScheduleTable.select(0, 0, 'order')
        users = UserTable.select(0, 0, 'order')
        return (my_type, (schedules, users))

    elif my_type == 2:
        schedules = FinalScheduleTable.select(0, 'order')
        users = FinalUserTable.select(0, 'order')
        return (my_type, (schedules, users))
        
# clear user
def userclear():

    users = FinalUserTable.select(0, 'all')

    for user in users:
        FinalUserTable.update(user.s_name, '0', 'Nov')

# clear schedule
def scheduleclear():

    schedules = FinalScheduleTable.select(0, 'all')
    for schedule in schedules:
        sid = schedule.id
        FinalScheduleTable.update(sid, '0', 0, '0', 'FsCh')


