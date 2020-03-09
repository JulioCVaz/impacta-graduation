
# Escreva um programa em Python3 que peça o valor do lado de um hexágono regular, calcule e imprima sua área e seu perímetro.
# Sabemos que um hexágono regular é o polígono de 6 lados iguais e com todos os ângulos internos iguais entre si.

import math;

QTD_LADOS_HEXAGONO = 6;

def calcAreaTrianguloEquilatero(lado):
    return ((lado ** 2) * math.sqrt(3)) / 4;

def calcAreaHexagonoRegular(lado):
    return calcAreaTrianguloEquilatero(lado) * QTD_LADOS_HEXAGONO;

def calculaPerimetro(lado):
    return lado * QTD_LADOS_HEXAGONO;

def processaValor():
    valor = float(input());
    return print(f'Lado do hexagono: {valor} metros,\nArea: {calcAreaHexagonoRegular(valor)} metros quadrados,\nPerimetro: {calculaPerimetro(valor)} metros.');

processaValor();
