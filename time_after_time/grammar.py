#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyparsing import oneOf
from parser import echo


DAY_NAME_VALUES = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]
SHORT_DAY_NAME_VALUES = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

DAY_SPEC = oneOf(" ".join(DAY_NAME_VALUES), caseless=True)("day")
DAY_SPEC.setParseAction(echo)

TIME_EXPRESSION = (DAY_SPEC)

# vim: filetype=python
