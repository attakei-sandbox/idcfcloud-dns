# -*- coding:utf8 -*-
"""Comannd base test
"""
from idcfcloud_dns import command


class ParserTests(object):
    def test_has_command(self):
        try:
            args = command.parser.parse_args(['list'])
        except SytemExit:
            args = None
        assert args.command == 'list'
