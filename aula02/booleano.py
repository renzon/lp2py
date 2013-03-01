# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals







b=True

if b:
    print "b é verdadeiro"
b=False
print b

def testar_booleano(b):
    if b:
        print "é verdadeiro"
    else:
        print "é falso"


print "Testar 0"
testar_booleano(0)

print "Testar -1"
testar_booleano(-1)

print "Testar string a"
testar_booleano("a")

print "Testar string vaziz"
testar_booleano("")

print 0==None

