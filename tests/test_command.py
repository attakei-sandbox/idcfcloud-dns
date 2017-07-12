# -*- coding:utf8 -*-
"""Comannd base test
"""
import pytest
from mock import MagicMock
from idcfcloud_dns import command


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
    @pytest.mark.with_network
    def test_no_zones(self, capsys):
        from argparse import Namespace
        cli_args = Namespace(command='llist')
        setting = MagicMock()
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
