# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

class Calculadora(object):
    def __init__(self):
        self.operacoes={}
        self.args=[]
        self.sinal="+"

    def calcular(self):
        operacao=self.operacoes[self.sinal]
        return operacao.calcular(*self.args)

    def adicionar_operacao(self,operacao):
        self.operacoes[operacao.sinal]=operacao

    def obter_inputs(self):
        raise NotImplementedError("necessario implementar obtencao de inputs")


class CalculadoraPrefixa(Calculadora):
    def obter_inputs(self):
        self.sinal=raw_input("Digite o sinal")
        operacao_escolhida=self.operacoes[self.sinal]
        numero_de_argumentos=operacao_escolhida.numero_de_argumentos
        self.args=[]
        for i in range(numero_de_argumentos):
            arg=input("Digite o argumento %s: "%(i+1))
            self.args.append(arg)

class Adicao(object):
    def __init__(self):
        self.sinal="+"
        self.numero_de_argumentos=2

    def calcular(self,a,b):
        return a+b

class Fatorial(object):
    def __init__(self):
        self.sinal="!"
        self.numero_de_argumentos=1

    def calcular(self,a):
        if a<=0:
            return 1
        return a*self.calcular(a-1)




calculadora=CalculadoraPrefixa()
calculadora.adicionar_operacao(Adicao())
calculadora.adicionar_operacao(Fatorial())
calculadora.obter_inputs()
print calculadora.calcular()