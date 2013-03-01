# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

class Pessoa():
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

    def cumprimentar(self):
        return "Olá meu nome é "+self.nome

if __name__=="__main__":
    renzo= Pessoa("Renzo",30)
    print renzo.cumprimentar()
    print type(renzo)
    if isinstance(renzo,Pessoa):
        print "Eh do tipo Pessoa"
    else:
        print "Não é do tipo Pessoa"

    joao=Pessoa("Joao",20)
    joao.segundo_nome="Lucas"
    print joao.segundo_nome
    print renzo.segundo_nome


# print __name__

