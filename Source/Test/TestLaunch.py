#!/usr/bin/env python
# coding: utf-8
import web
import sys
sys.path.append("..")
import index
import urllib

# Test '/schedule/launch'
class TestLaunch():
    def setUp(self):
        self.app = index.app

        # Login
        self.data = urllib.urlencode({'s_id': 'admin', 's_pass': 'admin'}) 
        self.app.request('/schedule/login', method='POST', data=self.data)

    def test(self):
        result = self.app.request('/schedule/launch')

        # Launch successfully
        assert result.status == '303 See Other'