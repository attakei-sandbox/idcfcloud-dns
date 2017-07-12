# -*- coding:utf8 -*-
"""Module for command line."""
import sys
import argparse
import json
import httplib2


parser = argparse.ArgumentParser()
parser.add_argument('command')


class ListCommand(object):
    """Command class to display list of zones."""

    def __init__(self, setting, cli_args): # noqa: flake8
        # type: (.Setting, argparse.Namespace) -> None
        self.setting = setting
        self.cli_args = cli_args

    def run(self):
        # type: () -> int
        """Run main logic of command.

        :return: status code
        :rtype: int
        """
        http = httplib2.Http()
        (resp, content) = http.request(
            'https://dns.idcfcloud.com/api/v1/zones')
        # type: ( httplib2.Response, str)
        if resp.status == 401:
            data = json.loads(content)
            sys.stderr.write(data['message'])
            return 1
        return 0
