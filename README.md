time-after-time
===============

[![Build Status](https://travis-ci.org/ryankanno/time-after-time.png?branch=master)](https://travis-ci.org/ryankanno/time-after-time)
[![Coverage Status](https://coveralls.io/repos/ryankanno/time-after-time/badge.png)](https://coveralls.io/r/ryankanno/time-after-time)

Tiny grammar is tiny. Tiny library to parse out various time grammars
describing the future.

At a minimum, supporting the following: (this list will grow)

  - 1 hour[hr]....24 hour[hr]
  - in 2 hours[months,weeks,days,minutes,seconds]
  - next monday[mon]
  - tomorrow

TODO
====

  * Currently, supports only a time, needs to return the notion of a point in
    time (ie a timestamp).
