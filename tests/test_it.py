# -*- coding:utf8 -*-
"""Comannd base test
"""
import os
import mock
from idcfcloud_dns import find_settings



class TestSettingsFromEnv(object):
    @mock.patch.dict(os.environ, {'IDCF_DNS_API_KEY': 'my_key'})
    def test_use_env(self):
        setting = find_settings()
        assert setting.api_key == 'my_key'

    @mock.patch.dict(os.environ, {'IDCF_DNS_SECRET_KEY': 'my_secret'})
    def test_use_env(self):
        setting = find_settings()
        assert setting.secret_key == 'my_secret'
