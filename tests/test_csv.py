#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import raises
from pyparsing import ParseException
from time_after_time.grammar import TIME_EXPRESSION
import unittest


class TestGrammar(unittest.TestCase):

    def test_day_names(self):
        days = """\
            Monday
            Tuesday
            Wednesday
            Thursday
            Friday
            Saturday
            Sunday""".splitlines()
        for day in days:
            TIME_EXPRESSION.parseString(day)

    @raises(ParseException)
    def test_invalid_grammar(self):
        days = """\
            Monday
            Tuesd""".splitlines()
        for day in days:
            TIME_EXPRESSION.parseString(day)

# vim: filetype=python
