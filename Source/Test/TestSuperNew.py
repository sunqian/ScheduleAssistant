#!/usr/bin/env python
# coding: utf-8
import web
import sys
sys.path.append("..")
import index
import urllib

# Test '/schedule/superusernew'
class TestSuperNew():
    def setUp(self):
        self.app = index.app

        # Register
        self.data = urllib.urlencode({'s_id': '123', 's_name': '123', 's_pass': '123', 'test_pass': '123'}) 
        self.app.request('/schedule/register', method='POST', data=self.data)

        # Login
        self.data = urllib.urlencode({'s_id': 'admin', 's_pass': 'admin'}) 
        self.newdata = urllib.urlencode({'s_name': '123', 's_time': '14'}) 
        self.app.request('/schedule/login', method='POST', data=self.data)

    def test(self):
        result = self.app.request('/schedule/superusernew', method='POST', data=self.newdata)
        
        # Success
        assert result.status == '303 See Other'
