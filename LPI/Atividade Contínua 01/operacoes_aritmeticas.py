#Escreva um programa em Python3 que receba um número real positivo e não nulo, calcule e imprima o resultado das seguintes operações aritméticas:

import math

# funcao para calculcar potencia ao quadrado
def calcPotencia(valor):
    return valor ** 2;  

#funcao para calcular potencia elevada a n
def calcPotenciaN(valor):
    #eulers = 2.71828 ou math.e;
    return valor ** math.e;

#funcao para calculcar raiz quadrada
def calcRaizQuadrada(valor):
    return math.sqrt(valor);

#funcao para calculcar raiz ao cubo
def calcRaizCubica(valor):
    # n + . converte o número para float
    return valor ** (1./3.);

#funcao para calculcar raiz elevado a n
def calcRaizN(valor):
    return valor ** (1./valor); # checar matematicamente se está correto

#funcao para calcular multiplicacao
def calcMultiplicacao(valor):
    return math.e * valor

#funcao para calculcar divisao de Pi
def calcDivisaoPi(valor):
    return math.pi / valor;

#funcao para calcular log de 7 a N
#def calcLog7(valor):
    # return 
#funcao para calcular log de e
# def calcLogE():

#funcao apra calculcar log de pi
# def calcLogPi():


def processaValor():
    valor  = float(input());
    
    potencia = calcPotencia(valor);
    potencia_n = calcPotenciaN(valor);
    raiz_quadrada = calcRaizQuadrada(valor); 
    raiz_cubica = calcRaizCubica(valor);
    raiz_n = calcRaizN(valor);
    multiplicacao = calcMultiplicacao(valor);
    divisao = calcDivisaoPi(valor);

    print(divisao);

processaValor();