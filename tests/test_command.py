# -*- coding:utf8 -*-
"""Comannd base test
"""
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
