time-after-time
===============

[![Build Status](https://travis-ci.org/ryankanno/time-after-time.png?branch=master)](https://travis-ci.org/ryankanno/time-after-time)
[![Coverage Status](https://coveralls.io/repos/ryankanno/time-after-time/badge.png)](https://coveralls.io/r/ryankanno/time-after-time)

Tiny grammar is tiny. Tiny library to parse out various time grammars
describing the future.

At a minimum, *should* support the following: (this list will grow) 

(<del>means it is supported</del>)

  - Relative time with respect to now
    - <del>1 h[m,w,d,min,s]</del>
    - 3w2d30s
  - Specific day/time from now
    - monday[mon]
    - monday!12.15pm
    - mon!2315

TODO
====

  * Currently, supports only a time, needs to return the notion of a point in
    time (ie a timestamp).
