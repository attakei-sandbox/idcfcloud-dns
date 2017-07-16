# -*- coding:utf8 -*-
"""Comannd base test
"""
import pytest
import os
import json
from mock import MagicMock, patch
from idcfcloud_dns import command


def mocked_request(status, content):
    response = MagicMock()
    response.status = status
    content = json.dumps(content)
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

    def test_no_zones(self, capsys):
        from argparse import Namespace
        cli_args = Namespace(command='llist')
        setting = dummy_settings()
        mocked_content = []
        with patch('httplib2.Http') as Mock:
            inst = Mock.return_value
            inst.request.return_value = mocked_request(200, mocked_content)
            cmd = command.ListCommand(setting, cli_args)
            ret, out, err = self._run_and_capture(cmd, capsys)
        assert ret == 0
        assert out == ''

    def test_one_zone(self, capsys):
        from argparse import Namespace
        cli_args = Namespace(command='llist')
        setting = dummy_settings()
        mocked_content = [
            {'name': 'example.com', 'description': 'My zone'}
        ]
        with patch('httplib2.Http') as Mock:
            inst = Mock.return_value
            inst.request.return_value = mocked_request(200, mocked_content)
            cmd = command.ListCommand(setting, cli_args)
            ret, out, err = self._run_and_capture(cmd, capsys)
        assert ret == 0
        assert 'example.com' in out
        assert 'My zone' in out

    def test_on_error(self, capsys):
        from argparse import Namespace
        cli_args = Namespace(command='list')
        setting = dummy_settings()
        mocked_content = {'message': 'invalid apikey'}
        with patch('httplib2.Http') as Mock:
            inst = Mock.return_value
            inst.request.return_value = mocked_request(401, mocked_content)
            cmd = command.ListCommand(setting, cli_args)
            ret, out, err = self._run_and_capture(cmd, capsys)
        assert ret == 1
        assert err == 'invalid apikey'
