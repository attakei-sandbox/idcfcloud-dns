# -*- coding:utf8 -*-
"""HTTP requests module."""
from __future__ import unicode_literals
import hmac
import hashlib
from base64 import b64encode


def build_signature(method, path, api_key, secret_key, expires):
    """Build API request signature.

    :param method: request method
    :type method: basestring
    :param path: request path (not contain host and protcol)
    :type path: basestring
    :param api_key: API key
    :type api_key: basestring
    :param secret_key: API secret key
    :type secret_key: basestring
    :param expires: Expires of API request
    :type expires: int
    :returns: signature
    :rtype: basestring
    """
    base_string = u'\n'.join([
            method, path, api_key, str(expires), ''
        ]).encode()
    hash = hmac.new(secret_key.encode(), base_string, hashlib.sha256)
    return b64encode(hash.digest())
