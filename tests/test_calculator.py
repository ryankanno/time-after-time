#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from nose.tools import ok_
from time_after_time.grammar import time_expression
import unittest


class TestMilitaryCalculator(unittest.TestCase):

    def test_specific_military_time(self):
        parsed_time = time_expression.parseString("2359")
        ok_(parsed_time["time"] == datetime.time(hour=23, minute=59))

        parsed_time = time_expression.parseString("0001")
        ok_(parsed_time["time"] == datetime.time(hour=0, minute=1))


class TestTwelveHourTimeCalculator(unittest.TestCase):

    def test_specific_twelve_hour_time(self):
        parsed_time = time_expression.parseString("12:15 AM")
        ok_(parsed_time["time"] == datetime.time(hour=0, minute=15))

# vim: filetype=python
