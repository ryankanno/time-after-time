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

    def _should_adjust_for_pm(self, hour):
        return 'am_pm' in self.tokens and self.tokens.am_pm.lower() == 'pm' \
            and hour != 12

    def _should_adjust_for_am(self, hour):
        return 'am_pm' in self.tokens and self.tokens.am_pm.lower() == 'am' \
            and hour == 12

    def _calculate_time(self):
        hour, minute = 0, 0
        if 'twelve_hour_clock_time' in self.tokens:
            if 'hour' in self.tokens:
                hour = self.tokens.hour
            if 'minute' in self.tokens:
                minute = self.tokens.minute
            if self._should_adjust_for_am(hour):
                hour -= 12
            elif self._should_adjust_for_pm(hour):
                hour += 12
            time = datetime.time(hour=hour, minute=minute)
            return time

# vim: filetype=python
