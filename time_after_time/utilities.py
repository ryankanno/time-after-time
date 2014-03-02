#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyparsing import CaselessLiteral
from pyparsing import Combine
from pyparsing import Optional

CL = CaselessLiteral


def create_plural_tokens(iterable_of_str):
    plural = lambda s: Combine(CL(s) + Optional(CL("s")))
    return map(plural, iterable_of_str)

# vim: filetype=python
