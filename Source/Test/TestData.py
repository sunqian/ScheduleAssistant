#!/usr/bin/env python
# coding: utf-8
import web
import sys
sys.path.append("..")
import index
import urllib

# Test '/schedule/data'
class TestData():
    def setUp(self):
        self.app = index.app

        # Login
        self.data = urllib.urlencode({'s_id': 'public', 's_pass': 'public'}) 
        self.app.request('/schedule/login', method='POST', data=self.data)

    def test(self):
        result = self.app.request('/schedule/data')

        # Redirect successfully
        assert result.status == '303 See Other'
