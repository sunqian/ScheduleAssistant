#!/usr/bin/env python
# coding: utf-8
import web
from Controller import RegisterManager
from Config import settings
from Config.url import urls

render = settings.render

class Register:

    def GET(self):
        return render.register()

    def POST(self):
        i = web.input()
        my_id = i.get('s_id')
        my_name = i.get('s_name')
        my_pass = i.get('s_pass')
        test_pass = i.get('test_pass')

        if(test_pass != my_pass):
            return render.error('两次输入的密码不一致', None)

        result = RegisterManager.register(my_id, my_name, my_pass)

        if result == 'Existed':
            return render.error('用户已存在', None)
        
        if result == 'RGSuccess':
            return render.error('注册成功', '/')
