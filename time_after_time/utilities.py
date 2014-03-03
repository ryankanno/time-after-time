#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyparsing import CaselessLiteral
from pyparsing import Combine
from pyparsing import Optional

CL = CaselessLiteral

SHORT_TO_FULL_UNITS = {
    'y': 'year',
    'm': 'month',
    'w': 'week',
    'd': 'day',
    'h': 'hour',
    'min': 'minute',
    's': 'second'
}


def add_s_to_text(text):
    if text[-1] == 's':
        return text
    return text + 's'


def create_plural_tokens(iterable_of_str):
    plural = lambda s: Combine(CL(s) + Optional(CL("s")))
    return map(plural, iterable_of_str)


def create_relative_delta_args_from_tokens(tokens):
    relative_delta_args = {}
    time_unit = tokens.time_units.lower()
    if time_unit and time_unit in SHORT_TO_FULL_UNITS:
        time_unit = SHORT_TO_FULL_UNITS[time_unit]

    time_unit = add_s_to_text(time_unit)
    relative_delta_args[time_unit] = 1
    if tokens.quantity:
        relative_delta_args[time_unit] = tokens.quantity

    return relative_delta_args

# vim: filetype=python
