#!/usr/bin/env python
# coding: utf-8
import web
import sys
sys.path.append("..")
import index
import urllib

# Test '/schedule/login'
class TestLogin():
    def setUp(self):
        self.app = index.app

        self.data = urllib.urlencode({'s_id': 'admin', 's_pass': 'admin'}) 

    def test(self):
        result = self.app.request('/schedule/login', method='POST', data=self.data)

        # Login successfully
        assert result.status == '303 See Other'