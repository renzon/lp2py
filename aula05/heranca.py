# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gi.types import mro
from aula03.pessoa import Pessoa


class Homem(Pessoa):
    def jogar_bola(self):
        return self.nome+" jogando bola"

    def cumprimentar(self):
        return self.nome+" apertando mãos"

class Mulher(Pessoa):
    def fazer_maquiagem(self):
        return self.nome+" fazendo maquiagem"

    def cumprimentar(self):
        return self.nome+" beijando 3 vezes"

def jogar_futebol(pessoa):
    print pessoa.jogar_bola()

class Hermafrodita(Homem,Mulher):
    def cumprimentar(self):
        return Mulher.cumprimentar(self)

homem=Homem("Renzo",30)
mulher=Mulher("Juliana",20)
print homem.cumprimentar(), homem.jogar_bola()
print mulher.cumprimentar(), mulher.fazer_maquiagem()
hermafrodita=Hermafrodita("Lady Gaga",40)
print hermafrodita.nome,hermafrodita.idade
print hermafrodita.fazer_maquiagem()
print hermafrodita.jogar_bola()
print hermafrodita.cumprimentar()
print mro(Hermafrodita)
