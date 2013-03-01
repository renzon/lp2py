# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

def gerador_de_derivada(f):
    def derivada(x):
        deltax=0.00000000001
        return (f(x+deltax)-f(x))/deltax
    return derivada

def reta(x):
    return x+1

derivada_da_reta=gerador_de_derivada(reta)

print derivada_da_reta(0)


def parabola(x):
    return x*x

derivada_da_parabola=gerador_de_derivada(parabola)

print derivada_da_parabola(0)
print derivada_da_parabola(1)
print derivada_da_parabola(2)
