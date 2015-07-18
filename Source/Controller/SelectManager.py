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

class Strike:

    def GET(self, sid):

        schedule = ScheduleTable.select(sid, 0, 'id')
        name = schedule[0].s_name
        user = UserTable.select(0, name, 'name')
        duty = user[0].time_duty - 1
        ScheduleTable.update(sid, '0')

        UserTable.update(name, duty)
        raise web.seeother('/schedule/data')

class Strikeundo:

    def GET(self, sid):

        schedule = ScheduleTable.select(sid, 0, 'id')
        name = schedule[0].s_name
        user = UserTable.select(0, name, 'name')
        duty = user[0].time_duty + 1

        ScheduleTable.update(sid, '1')
        UserTable.update(name, duty)
        raise web.seeother('/schedule/data')


class Launch:
    
    def GET(self):
        
        finalschedules = FinalScheduleTable.select(0, 'all')
        finalusers = FinalUserTable.select(0, 'all')
        schedules = ScheduleTable.select(0, 0, 'all')
        users = UserTable.select(0, 0, 'all')

        for finalschedule in finalschedules:
            FinalScheduleTable.delete()

        for finaluser in finalusers:
            name = finaluser.s_name

            FinalUserTable.delete(name)

        for schedule in schedules:
            if schedule.keep:
                FinalScheduleTable.insert(schedule.s_name, schedule.s_time)
            else:
                sid=schedule.id

                ScheduleTable.delete(sid, 0, 'id')

        for user in users:
            if user.s_type == 0:
                FinalUserTable.insert(user.s_name, user.time_duty)
        raise web.seeother('/schedule/data')

        
