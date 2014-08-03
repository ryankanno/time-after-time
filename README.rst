time-after-time
===============

.. image:: https://travis-ci.org/ryankanno/time-after-time.png?branch=master
   :target: https://travis-ci.org/ryankanno/time-after-time

.. image:: https://coveralls.io/repos/ryankanno/time-after-time/badge.png
   :target: https://coveralls.io/r/ryankanno/time-after-time

Tiny grammar is tiny. Tiny library to parse out various time grammars
describing the future.

At a minimum, *should* support the following: (this list will grow) 

(&#10003; means it is supported)

  - Relative time with respect to now
    - &#10003; 1 h[m,w,d,min,s]
    - &#10003; 3w2d30s
  - Specific time today
    - &#10003; 12.15 a[p]m
    - &#10003; 2359
  - Specific day/time from now
    - monday[mon]
    - monday!12.15pm
    - mon!2315

TODO
====

  * Currently, supports only a time, needs to return the notion of a point in
    time (ie a timestamp).
  * Write out BNF
