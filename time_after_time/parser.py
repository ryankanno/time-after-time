#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .calculator import MilitaryDateTimeCalculator
from .calculator import RelativeDateTimeCalculator
from .calculator import TwelveHourDateTimeCalculator
import datetime
from .utilities import create_relative_delta_args_from_tokens


def calculate_time_offset(s, loc, toks):
    args = create_relative_delta_args_from_tokens(toks)
    toks["relative_time_offset_args"] = args


def calculate_time(s, loc, toks):
    if toks.twelve_hour_clock_time:
        calc = TwelveHourDateTimeCalculator(toks)
    elif toks.military_time:
        calc = MilitaryDateTimeCalculator(toks)
    else:
        calc = RelativeDateTimeCalculator(toks)

    time = calc.calculate()
    toks["time"] = time


# ugly, but a way i could test, so im fine with it
def inject_point_of_time(s, loc, toks):
    if toks.test:
        toks["absolute_point_in_time"] = datetime.datetime.utcfromtimestamp(0)


def parse_int(s, loc, toks):
    return int(toks[0])


# vim: filetype=python
