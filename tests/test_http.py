# -*- coding:utf8 -*-
"""HTTP modules tests
"""
from __future__ import unicode_literals
from idcfcloud_dns import http


def test_build_signature():
    signature = http.build_signature('GET', '/', 'API_KEY', 'SECRET_KEY', 1)
    assert isinstance(signature, basestring)
    assert len(signature) != 0
