# -*- coding:utf8 -*-
"""FuncTest for commands.

In this module, all test cases are marked 'functest' to skip unittest.
"""
import pytest
import os
import sys
import subprocess
from mock import patch


@pytest.mark.functest
class TestListCommand(object):
    @patch.dict('os.environ', 
        {   'IDCF_DNS_API_KEY': os.environ['FUNCTEST_API_KEY'],
            'IDCF_DNS_SECRET_KEY': os.environ['FUNCTEST_SECRET_KEY'],
        })
    @patch.object(sys, 'argv', ['_', 'list'])
    def test_no_zones(self, capsys):
        from idcfcloud_dns.command import main
        ret = main()
        assert ret == 0

    @patch.dict('os.environ', 
        {   'IDCF_DNS_API_KEY': 'dummy_api_key',
            'IDCF_DNS_SECRET_KEY': 'dummy_secret_key',
        })
    @patch.object(sys, 'argv', ['_', 'list'])
    def test_invalid_apikey(self, capsys):
        from idcfcloud_dns.command import main
        ret = main()
        assert ret == 1
        out, err = capsys.readouterr()
        assert 'invalid apikey' in err
