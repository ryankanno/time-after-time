#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import datetime


class DateTimeCalculator(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, tokens):
        self.tokens = tokens

    def _calculate_day(self):
        return datetime.date.today()

    @abc.abstractmethod
    def _calculate_time(self):
        return

    def calculate(self):
        day = self._calculate_day()
        time = self._calculate_time()
        return datetime.datetime.combine(day, time)


class MilitaryDateTimeCalculator(DateTimeCalculator):
    def __init__(self, tokens):
        super(MilitaryDateTimeCalculator, self).__init__(tokens)

    def _calculate_time(self):
        if 'military_time' in self.tokens:
            military_time = self.tokens.military_time
            return datetime.time(hour=int(military_time[0:2]),
                                 minute=int(military_time[2:4]))


class TwelveHourDateTimeCalculator(DateTimeCalculator):
    def __init__(self, tokens):
        super(TwelveHourDateTimeCalculator, self).__init__(tokens)

    def _calculate_time(self):
        hours, minutes = 0, 0
        if 'twelve_hour_clock_time' in self.tokens:
            if 'hours' in self.tokens:
                hours = self.tokens.hour
            if 'minutes' in self.tokens:
                minutes = self.tokens.minutes
            time = datetime.time(hour=hours, minute=minutes)
            return time

# vim: filetype=python
