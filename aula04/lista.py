# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

lista=["a","b","b","c"]






tamanho= len(lista)
lista.append("d")
lista.remove("b")
del lista[0];
for i,v in enumerate(lista):
    print i,v


inteiros=[1,2,3,4,5,6,7,8,9,10]
inteiros=[i+1 for i in inteiros if i%2!=0]
print inteiros
