# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

dct={0:"zero",1:"um",2:"dois"}






celular="01201201000"
extenso=[dct[int(char)] for char in celular]
extenso="####".join(extenso)
print extenso

for k,v in dct.iteritems():
    print k,v


