#!/usr/bin/env python
# coding: utf-8
import web
import sys
sys.path.append("..")
import index
import urllib

# Test '/schedule/(\d+)/userdelete'
class TestUserDelete():
    def setUp(self):
        self.app = index.app

        # Register
        self.data = urllib.urlencode({'s_id': '123', 's_name': '123', 's_pass': '123', 'test_pass': '123'}) 
        self.app.request('/schedule/register', method='POST', data=self.data)

        # Login
        self.data = urllib.urlencode({'s_id': 'admin', 's_pass': 'admin'}) 
        self.app.request('/schedule/login', method='POST', data=self.data)

    def test(self):
        result = self.app.request('/schedule/123/userdelete')

        # Delete user successfully
        assert result.status == '303 See Other'