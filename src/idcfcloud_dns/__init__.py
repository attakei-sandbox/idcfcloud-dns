#!/usr/bin/env python
# -*- coding:utf8 -*-
"""TOp module."""
import os

__version__ = '0.0.1'


class Setting():
    """Pacage settings model.

    Read environments.
    """

    def __init__(self):
        """Parameter is read from environments."""
        self._api_key = os.environ.get('IDCF_DNS_API_KEY')
        self._secret_key = os.environ.get('IDCF_DNS_SECRET_KEY')

    @property
    def api_key(self):
        """IDCF-cloud DNS API key.

        :rtype: str
        """
        return self._api_key

    @property
    def secret_key(self):
        """IDCF-cloud DNS secret key.

        :rtype: str
        """
        return self._secret_key


def find_settings():
    """Load and return setting.

    :rtype: Setting
    """
    return Setting()
