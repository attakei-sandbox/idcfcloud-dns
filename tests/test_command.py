# -*- coding:utf8 -*-
"""Comannd base test
"""
import pytest
import os
import json
from mock import MagicMock, patch
from idcfcloud_dns import command


class MockedHttp(object):
    def request(self, *args, **kwargs):
        response = MagicMock()
        response.status = 200
        content = json.dumps([])
        return response, content


class TestParser(object):
    def test_has_command(self):
        from argparse import Namespace
        try:
            args = command.parser.parse_args(['list'])
        except SytemExit:
            args = None
        assert isinstance(args, Namespace)
        assert args.command == 'list'


class TestListCommand(object):
    @patch('httplib2.Http', MockedHttp)
    def test_no_zones(self, capsys):
        from argparse import Namespace
        cli_args = Namespace(command='llist')
        setting = MagicMock()
        setting.api_key = 'dummy_key'
        setting.secret_key = 'dummy_key'
        cmd = command.ListCommand(setting, cli_args)
        ret = cmd.run()
        out, err = capsys.readouterr()
        assert ret == 0
        assert out == ''

    @pytest.mark.with_network
    def test_invalid_key_pair(self, capsys):
        from argparse import Namespace
        cli_args = Namespace(command='list')
        setting = MagicMock()
        setting.api_key = 'dummy_key'
        setting.secret_key = 'dummy_key'
        cmd = command.ListCommand(setting, cli_args)
        ret = cmd.run()
        assert ret == 1
        out, err = capsys.readouterr()
        assert out == ''
        assert err == 'invalid apikey'
