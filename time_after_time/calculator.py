#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TimeCalculator(object):
    def __init__(self, tokens):
        self.tokens = tokens


class MilitaryTimeCalculator(TimeCalculator):
    def __init__(self, tokens):
        super(MilitaryTimeCalculator, self).__init__(tokens)

    def calculate(self):
        if 'military_time' in self.tokens:
            pass


class TwelveHourTimeCalculator(TimeCalculator):
    def __init__(self, tokens):
        super(TwelveHourTimeCalculator, self).__init__(tokens)

    def calculate(self):
        if 'twelve_hour_clock_time' in self.tokens:
            pass

# vim: filetype=python
