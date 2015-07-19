#!/usr/bin/env python
# coding: utf-8
import web
import sys
sys.path.append("..")
import index
import urllib

# Test '/schedule/(\d+)/delete'
class TestDelete():
    def setUp(self):
        self.app = index.app

        # Login
        self.data = urllib.urlencode({'s_id': 'admin', 's_pass': 'admin'}) 
        self.app.request('/schedule/login', method='POST', data=self.data)

    def test(self):
        result = self.app.request('/schedule/1/delete')

        # Delete successfully
        assert result.status == '200 OK'
