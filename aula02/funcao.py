# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def a():
    print "Chamando a"

b=a

print type(b)
b()

def gerador_de_funcao(argumento):
    def f():
        argumento+=1
        print argumento
    return f

f_0=gerador_de_funcao()

f_0()
f_0()



