#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
from pyparsing import CaselessLiteral
from pyparsing import nums
from pyparsing import oneOf
from pyparsing import Optional
from pyparsing import StringEnd
from pyparsing import Suppress
from pyparsing import Word
from parser import echo
from parser import parse_int
from utilities import create_plural_tokens


CL = CaselessLiteral

DAYS_OF_WEEK = oneOf(list(calendar.day_name))
ABBR_DAYS_OF_WEEK = oneOf(list(calendar.day_abbr))

AM, PM = CL("AM"), CL("PM")
COLON = Suppress(':')
TODAY, TOMORROW = CL("Today"), CL("Tomorrow")
NOON, MIDNIGHT = CL("Noon"), CL("Midnight")

YEAR, MONTH, WEEK, DAY = create_plural_tokens("Year Month Week Day".split())
HOUR, MINUTE, SECOND = create_plural_tokens("Hour Minute Second".split())

Y, MON, W, D, H, MIN, S = map(CL, "Y MON W D H MIN S".split())

TIME_UNITS = (YEAR | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND |
              Y | MON | W | D | H | MIN | S)

TIME_DIGITS = Word(nums, min=1, max=2).setParseAction(parse_int)
INT = Word(nums).setParseAction(parse_int)

# specific day
day_spec = DAYS_OF_WEEK("day") | ABBR_DAYS_OF_WEEK("day")
day_spec.setParseAction(echo)

# relative time
rel_time_spec = INT("quantity") + TIME_UNITS("time-units")

# specific time
time_spec = TIME_DIGITS("HH") + \
    Optional(COLON + TIME_DIGITS("MM")) + \
    Optional(COLON + TIME_DIGITS("SS")) + \
    (AM | PM)("am-pm")
time_spec.setParseAction(echo)

time_expression = (rel_time_spec | time_spec | day_spec) + StringEnd()

# vim: filetype=python
