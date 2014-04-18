#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import raises
from pyparsing import ParseException
from time_after_time.grammar import time_expression
import unittest


class TestGrammar(unittest.TestCase):

    def test_relative_time_wrt_now(self):
        relative_times = """\
            1y
            1 y
            1 year
            2 years
            1m
            1 m
            1 month
            2 months
            1d
            1 d
            1 day
            2 days
            1h
            1 h
            1 hour
            2 hours
            1min
            1 min
            1 minute
            1 minutes
            1s
            1 s
            1 second
            2 seconds""".splitlines()
        for relative_time in relative_times:
            time_expression.parseString(relative_time)

    def test_specific_twelve_hour_clock_time(self):
        times = """\
            12:12 am
            23:10 pm
            12 pm
            12:15 am""".splitlines()
        for time in times:
            time_expression.parseString(time)

    def test_specific_military_time(self):
        times = """\
            2359
            0100
            0210
            0321
            0700""".splitlines()
        for time in times:
            time_expression.parseString(time)

    @raises(ParseException)
    def test_invalid_grammar_almost_complete(self):
        time_expression.parseString("Monda")

    @raises(ParseException)
    def test_invalid_grammar_repeating(self):
        time_expression.parseString("TueTue")

# vim: filetype=python
