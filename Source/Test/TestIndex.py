#!/usr/bin/env python
# coding: utf-8
import web
import sys
sys.path.append("..")
import index
import urllib

# Test '/'
class TestIndex():
    def setUp(self):
        self.app = index.app

    def test(self):
        result = self.app.request('/')
        assert result.status == '200 OK'
