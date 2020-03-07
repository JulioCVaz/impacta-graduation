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
def calcLog7(valor):
    return math.log(valor) / math.log(7);

#funcao para calcular log de e
def calcLogE(valor):
    return math.log(valor) / math.log(math.e);

#funcao apra calculcar log de pi
def calcLogPi(valor):
    return math.log(valor) / math.log(math.pi);

def processaValor():
    valor  = float(input());
    
    potencia = calcPotencia(valor);
    potencia_n = calcPotenciaN(valor);
    raiz_quadrada = calcRaizQuadrada(valor); 
    raiz_cubica = calcRaizCubica(valor);
    raiz_n = calcRaizN(valor);
    multiplicacao = calcMultiplicacao(valor);
    divisao = calcDivisaoPi(valor);
    log_7 = calcLog7(valor);
    log_e = calcLogE(valor);
    log_pi = calcLogPi(valor);

    print(f'i) {potencia}\nii) {potencia_n}\niii) {raiz_quadrada}\niv) {raiz_cubica}\nv) {raiz_n}\nvi) {multiplicacao}\nvii) {divisao}\nviii) {log_7}\nix) {log_e}\nx) {log_pi}');

processaValor();
