#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


class TimeCalculator(object):
    def __init__(self, tokens):
        self.tokens = tokens


class MilitaryTimeCalculator(TimeCalculator):
    def __init__(self, tokens):
        super(MilitaryTimeCalculator, self).__init__(tokens)

    def calculate(self):
        if 'military_time' in self.tokens:
            military_time = self.tokens.military_time
            return datetime.time(hour=int(military_time[0:2]),
                                 minute=int(military_time[2:4]))


class TwelveHourTimeCalculator(TimeCalculator):
    def __init__(self, tokens):
        super(TwelveHourTimeCalculator, self).__init__(tokens)

    def calculate(self):
        if 'twelve_hour_clock_time' in self.tokens:
            pass

# vim: filetype=python
