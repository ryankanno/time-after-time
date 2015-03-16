#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import datetime
from dateutil.relativedelta import relativedelta
from py_utilities.time.date_utilities import next_day


class DateTimeCalculator(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, tokens):
        self.tokens = tokens

    @abc.abstractmethod
    def _calculate_day(self):
        if 'day' in self.tokens:
            day = next_day(
                datetime.date.today(),
                self._get_isoweekday_from_str())
        else:
            day = datetime.date.today()
        return day

    @abc.abstractmethod
    def _calculate_time(self):
        raise NotImplementedError

    @abc.abstractmethod
    def calculate(self):
        day = self._calculate_day()
        time = self._calculate_time()
        return datetime.datetime.combine(day, time)

    def _get_isoweekday_from_str(self, day_as_str):
        return 1


class MilitaryDateTimeCalculator(DateTimeCalculator):
    def __init__(self, tokens):
        super(MilitaryDateTimeCalculator, self).__init__(tokens)

    def _calculate_day(self):
        return super(MilitaryDateTimeCalculator, self)._calculate_day()

    def _calculate_time(self):
        if 'military_time' in self.tokens:
            military_time = self.tokens.military_time
            return datetime.time(hour=int(military_time[0:2]),
                                 minute=int(military_time[2:4]))

    def calculate(self):
        return super(MilitaryDateTimeCalculator, self).calculate()


class RelativeDateTimeCalculator(DateTimeCalculator):
    def __init__(self, tokens):
        super(RelativeDateTimeCalculator, self).__init__(tokens)

    def _calculate_day(self):
        """ Not used """
        raise NotImplementedError

    def _calculate_time(self):
        """ Not used """
        raise NotImplementedError

    def calculate(self):
        time = self.tokens.absolute_point_in_time or datetime.datetime.now()
        if self.tokens.relative_time_offset_args:
            time += relativedelta(**(self.tokens.relative_time_offset_args))
        return time


class TwelveHourDateTimeCalculator(DateTimeCalculator):
    def __init__(self, tokens):
        super(TwelveHourDateTimeCalculator, self).__init__(tokens)

    def _should_adjust_for_pm(self, hour):
        return 'am_pm' in self.tokens and self.tokens.am_pm.lower() == 'pm' \
            and hour != 12

    def _should_adjust_for_am(self, hour):
        return 'am_pm' in self.tokens and self.tokens.am_pm.lower() == 'am' \
            and hour == 12

    def _calculate_day(self):
        return super(TwelveHourDateTimeCalculator, self)._calculate_day()

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

    def calculate(self):
        return super(TwelveHourDateTimeCalculator, self).calculate()

# vim: filetype=python
