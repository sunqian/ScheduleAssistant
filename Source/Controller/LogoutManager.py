#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls

def logout():
    web.ctx.session.kill()
