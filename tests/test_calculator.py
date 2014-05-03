#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from nose.tools import ok_
from time_after_time.grammar import time_expression
import unittest


class TestMilitaryCalculator(unittest.TestCase):

    def test_specific_military_time(self):
        expected_date = datetime.date.today()

        parsed_time = time_expression.parseString("2359")
        expected_time = datetime.time(hour=23, minute=59)
        expected_datetime = datetime.datetime.combine(expected_date,
                                                      expected_time)
        ok_(parsed_time["time"] == expected_datetime)

        parsed_time = time_expression.parseString("0001")
        expected_time = datetime.time(hour=0, minute=1)
        expected_datetime = datetime.datetime.combine(expected_date,
                                                      expected_time)
        ok_(parsed_time["time"] == expected_datetime)


class TestTwelveHourTimeCalculator(unittest.TestCase):

    def test_specific_twelve_hour_time(self):
        expected_date = datetime.date.today()
        parsed_time = time_expression.parseString("12.15 AM")
        expected_time = datetime.time(hour=0, minute=15)
        expected_datetime = datetime.datetime.combine(expected_date,
                                                      expected_time)
        ok_(parsed_time["time"] == expected_datetime)

        parsed_time = time_expression.parseString("4.20 pm")
        expected_time = datetime.time(hour=16, minute=20)
        expected_datetime = datetime.datetime.combine(expected_date,
                                                      expected_time)
        ok_(parsed_time["time"] == expected_datetime)

        parsed_time = time_expression.parseString("12.58 PM")
        expected_time = datetime.time(hour=12, minute=58)
        expected_datetime = datetime.datetime.combine(expected_date,
                                                      expected_time)
        ok_(parsed_time["time"] == expected_datetime)


# vim: filetype=python
