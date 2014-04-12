#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .calculator import TwelveHourTimeCalculator
from .calculator import MilitaryTimeCalculator
import datetime
from dateutil.relativedelta import relativedelta
from .utilities import create_relative_delta_args_from_tokens


def calculate_time_offset(s, loc, toks):
    args = create_relative_delta_args_from_tokens(toks)
    toks["relative_time_offset_args"] = args


def calculate_time(s, loc, toks):
    if toks.twelve_hour_clock:
        calc = TwelveHourTimeCalculator(toks)
        time = calc.calculate()
    elif toks.military_time:
        calc = MilitaryTimeCalculator(toks)
        time = calc.calculate()
    else:
        time = toks.absolute_point_in_time or datetime.datetime.now()

        if toks.relative_time_offset_args:
            time += relativedelta(**(toks.relative_time_offset_args))
    toks["time"] = time


# ugly, but a way i could test, so im fine with it
def inject_point_of_time(s, loc, toks):
    if toks.test:
        toks["absolute_point_in_time"] = datetime.datetime.utcfromtimestamp(0)


def parse_int(s, loc, toks):
    return int(toks[0])


# vim: filetype=python
