#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from dateutil.relativedelta import relativedelta
from utilities import create_relative_delta_args_from_tokens


def calculate_time_offset(s, loc, toks):
    args = create_relative_delta_args_from_tokens(toks)
    toks["relative_time_offset_args"] = args


def calculate_time(s, loc, toks):
    point_in_time = toks.point_in_time or datetime.datetime.now()

    if toks.relative_time_offset_args:
        point_in_time += relativedelta(**(toks.relative_time_offset_args))
    toks["time"] = point_in_time


def inject_point_of_time(s, loc, toks):
    if toks.test:
        toks["point_in_time"] = datetime.datetime.utcfromtimestamp(0)


def parse_int(s, loc, toks):
    return int(toks[0])


# vim: filetype=python
