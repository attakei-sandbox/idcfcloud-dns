# -*- coding:utf8 -*-
"""Comannd base test
"""
import pytest
import os
import json
from mock import MagicMock, patch
from idcfcloud_dns import command


class MockedHttp(object):
    content = []

    def request(self, *args, **kwargs):
        response = MagicMock()
        response.status = 200
        content = json.dumps(self.content)
        return response, content


def dummy_settings():
    setting = MagicMock()
    setting.api_key = 'dummy_key'
    setting.secret_key = 'dummy_key'
    return setting


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
    def _run_and_capture(self, command, capsys):
        ret = command.run()
        out, err = capsys.readouterr()
        return ret, out, err

    @patch('httplib2.Http', MockedHttp)
    def test_no_zones(self, capsys):
        MockedHttp.content = []
        from argparse import Namespace
        cli_args = Namespace(command='llist')
        setting = dummy_settings()
        cmd = command.ListCommand(setting, cli_args)
        ret, out, err = self._run_and_capture(cmd, capsys)
        assert ret == 0
        assert out == ''

    @patch('httplib2.Http', MockedHttp)
    def test_one_zone(self, capsys):
        MockedHttp.content = [
            {'name': 'example.com', 'description': 'My zone'}
        ]
        from argparse import Namespace
        cli_args = Namespace(command='llist')
        setting = dummy_settings()
        cmd = command.ListCommand(setting, cli_args)
        ret, out, err = self._run_and_capture(cmd, capsys)
        assert ret == 0
        assert 'example.com' in out
        assert 'My zone' in out

    @pytest.mark.with_network
    def test_invalid_key_pair(self, capsys):
        from argparse import Namespace
        cli_args = Namespace(command='list')
        setting = MagicMock()
        setting.api_key = 'dummy_key'
        setting.secret_key = 'dummy_key'
        cmd = command.ListCommand(setting, cli_args)
        ret, out, err = self._run_and_capture(cmd, capsys)
        assert ret == 1
        assert err == 'invalid apikey'
