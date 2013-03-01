# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

def f(*args):
    print args

f()
f(1)
f(1,2)

args=[1,2]

f(*args)
