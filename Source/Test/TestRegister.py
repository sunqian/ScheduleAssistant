#!/usr/bin/env python
# coding: utf-8
import web
import sys
sys.path.append("..")
import index
import urllib

# Test '/schedule/register'
class TestRegister():
    def setUp(self):
        self.app = index.app
        self.data = urllib.urlencode({'s_id': '123', 's_name': '123', 's_pass': '123', 'test_pass': '123'}) 

    def test(self):
        result = self.app.request('/schedule/register', method='POST', data=self.data)
        
        # Register successfully	
        assert result.status == '200 OK'