# -*- coding:utf8 -*-
"""Module for command line."""
import sys
import argparse
import json
import time
import httplib2
from .http import build_signature
from . import find_settings


parser = argparse.ArgumentParser()
parser.add_argument('command')


def main(argv=None):
    """Console entrypoint."""
    if argv is None:
        argv = sys.argv[1:]
    args = parser.parse_args(argv)
    setting = find_settings()
    command = ListCommand(setting, args)
    return command.run()


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
        expires = int(time.time()) + 60
        signature = build_signature(
            'GET', '/api/v1/zones',
            self.setting.api_key, self.setting.secret_key, expires)
        headers = {
            'X-IDCF-APIKEY': self.setting.api_key,
            'X-IDCF-Expires': str(expires),
            'X-IDCF-Signature': signature,
        }
        http = httplib2.Http()
        (resp, content) = http.request(
            'https://dns.idcfcloud.com/api/v1/zones',
            headers=headers)
        # type: ( httplib2.Response, str)
        if resp.status == 401:
            data = json.loads(content)
            sys.stderr.write(data['message'])
            return 1
        # TODO: No test
        if resp.status != 200:
            sys.stderr.write('Error\n')
            return 1
        # If API return "HTTP OK" and response json,
        # command render zone list (use domain)
        # TODO: No test
        data = json.loads(content)
        for zone in data:
            sys.stdout.write(zone['name'] + '\n')
        return 0
