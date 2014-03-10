#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TimeCalculator(object):
    def __init__(self, tokens):
        self.tokens = tokens


class MilitaryTimeCalculator(TimeCalculator):
    def __init__(self, tokens):
        super(MilitaryTimeCalculator, self).__init__(tokens)


class TwelveHourTimeCalculator(TimeCalculator):
    def __init__(self, tokens):
        super(TwelveHourTimeCalculator, self).__init__(tokens)

# vim: filetype=python
