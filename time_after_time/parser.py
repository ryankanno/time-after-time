#!/usr/bin/env python
# -*- coding: utf-8 -*-


def echo(toks):
    toks["results"] = toks[0]


def parse_int(token):
    return int(token[0])


# vim: filetype=python
