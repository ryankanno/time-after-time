#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
from .parser import calculate_time
from .parser import calculate_time_offset
from .parser import inject_point_of_time
from .parser import parse_int
from pyparsing import CaselessLiteral
from pyparsing import Forward
from pyparsing import nums
from pyparsing import oneOf
from pyparsing import Optional
from pyparsing import StringEnd
from pyparsing import Suppress
from pyparsing import Word
from .utilities import create_plural_tokens


# tokens
CL = CaselessLiteral

DAYS_OF_WEEK = oneOf(list(calendar.day_name))
ABBR_DAYS_OF_WEEK = oneOf(list(calendar.day_abbr))

AM, PM = CL("am"), CL("pm")
AT, AT_SYM = CL("at"), CL("!")
COLON = Suppress(':')
TEST = CL("test").setParseAction(inject_point_of_time)

YEAR, MONTH, WEEK, DAY = create_plural_tokens("year month week day".split())
HOUR, MINUTE, SECOND = create_plural_tokens("hour minute second".split())

Y, M, W, D, H, MIN, S = map(CL, "y m w d h min s".split())

TIME_UNIT = (YEAR | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND |
             MIN | Y | M | W | D | H | S)

TIME_DIGIT = Word(nums, min=1, max=2).setParseAction(parse_int)
INT = Word(nums).setParseAction(parse_int)

# relative to now
rel_daytime_spec = INT("quantity") + TIME_UNIT("time_units")
rel_daytime_specs = Forward()
rel_daytime_specs << rel_daytime_spec + Optional(rel_daytime_specs)

rel_daytime_spec_with_test = Optional(TEST("test")) + rel_daytime_specs
rel_daytime_spec_with_test.setParseAction(calculate_time_offset,
                                          calculate_time)

# specific day
day_spec = DAYS_OF_WEEK("day") | ABBR_DAYS_OF_WEEK("day")
day_spec.setParseAction(calculate_time)

# specific 12-hr time
twelve_hour_clock_time_spec = TIME_DIGIT("hour") + \
    Optional(COLON + TIME_DIGIT("minutes")) + \
    (AM | PM)("am_pm")
twelve_hour_clock_time_spec.setParseAction(calculate_time)

# specific military time
military_time_spec = Word(nums, min=4, max=4)
military_time_spec.setParseAction(calculate_time)

time_spec = (twelve_hour_clock_time_spec("twelve_hour_clock_time") |
             military_time_spec("military_time"))
abs_daytime_spec = (Optional(day_spec("specific_day")) +
                    time_spec("specific_time"))

# expression
time_expression = \
    (rel_daytime_spec_with_test("relative_daytime") | abs_daytime_spec) + \
    StringEnd()

# vim: filetype=python
