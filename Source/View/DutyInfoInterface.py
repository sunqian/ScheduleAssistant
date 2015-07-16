#!/usr/bin/env python
# coding: utf-8
import web
from Controller import DutyInfoManager
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'schedule'

class Info:

    def GET(self):
        result = DutyInfoManager.data()
        return render.info(result[1][1])

class Data:

    def GET(self):
        #session = web.config._session
        if web.ctx.session.loginned == 1:
            result = DutyInfoManager.data()
            my_type = result[0];

            if my_type == 0:
                return render.user(result[1])

            elif my_type == 1:
                return render.superuser(result[1][0], result[1][1])
            elif my_type == 2:

                return render.manage(result[1][0], result[1][1])
        raise web.seeother('/')


class Userclear:

    def GET(self):
        DutyInfoManager.userclear();

        raise web.seeother('/schedule/info')

class Scheduleclear:
    
    def GET(self):
        DutyInfoManager.scheduleclear()
        raise web.seeother('/schedule/data')
