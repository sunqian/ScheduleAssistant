#!/usr/bin/env python
# coding: utf-8
import web
from Controller import LogoutManager
from Config import settings
from Config.url import urls

class Logout:

    def GET(self):
        LogoutManager.logout()
        raise web.seeother('/')
