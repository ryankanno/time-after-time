#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from dateutil.relativedelta import relativedelta
from nose.tools import ok_
from time_after_time.grammar import time_expression
import unittest

EPOCH_DT = datetime.datetime.utcfromtimestamp(0)


class TestParser(unittest.TestCase):

    def test_single_relative_time_years(self):
        years_1 = """\
            test 1y
            test 1 y
            test 1 year""".splitlines()
        for year_1 in years_1:
            parsed_time = time_expression.parseString(year_1).time
            ok_(parsed_time == (EPOCH_DT + relativedelta(years=1)))

    def test_multi_relative_time_years(self):
        years_1 = """\
            test 1y2m""".splitlines()
        for year_1 in years_1:
            parsed_time = time_expression.parseString(year_1).time
            ok_(parsed_time == (EPOCH_DT + relativedelta(years=1, months=2)))
# vim: filetype=python
