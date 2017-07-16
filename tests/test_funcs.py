# -*- coding:utf8 -*-
"""FuncTest for commands.

In this module, all test cases are marked 'functest' to skip unittest.
"""
import pytest


@pytest.mark.functest
def test_it():
    assert True is True