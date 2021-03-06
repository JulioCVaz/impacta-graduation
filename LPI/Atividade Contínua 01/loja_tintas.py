# Imagine que você fora contratado para fazer um programa para uma loja de tintas, com o objetivo de calcular quantas latas de tinta são necessárias para pintar uma determinada área e calcular o preço final da compra.

# A loja trabalha com latas de tinta de:
# 24 litros, vendidas a R$91,00 cada e,
# 5.4 litros, vendidas a R$23,00 cada.
# Sabe-se ainda que cada litro de tinta cobre uma superfície de 7 metros quadrados.

# Faça um programa que receba o valor da área a ser pintada em metros quadrados, calcule e imprima:

# a) A quantidade de latas de tinta e o preço final, considerando apenas latas de 24 litros.
# b) A quantidade de latas de tinta e o preço final, considerando apenas latas de 5.4 litros.
# c) A quantidade de latas de tinta e o preço final, considerando ambas as latas, de 24 e 5.4 litros.

import math;

LATA_GRANDE_LTS = 24;
LATA_PEQUENA_LTS = 5.4;
PRECO_LTS_GRANDE = 91;
PRECO_LTS_PEQUENA = 23;


#Sabe-se ainda que cada litro de tinta cobre uma superfície de 7 metros quadrados.
def calcQtdLitros(area):
    return area / 7;

def calcQtdLatas(area):
    qtd_litros = calcQtdLitros(area);

    qtd_lata_grande = math.ceil(qtd_litros / LATA_GRANDE_LTS);
    qtd_lata_pequena = math.ceil(qtd_litros / LATA_PEQUENA_LTS);
    resto_grade = math.floor(qtd_litros / LATA_GRANDE_LTS);
    resto_pequena = math.ceil((qtd_litros % LATA_GRANDE_LTS) / LATA_PEQUENA_LTS);

    return [qtd_lata_grande, qtd_lata_pequena, resto_grade, resto_pequena];

def calcValorFinal(area):
    qtdLatas = calcQtdLatas(area);
    valorLtsGrade = qtdLatas[0] * PRECO_LTS_GRANDE;
    valorLtsPequena = qtdLatas[1] * PRECO_LTS_PEQUENA;
    valorLtsRestoGrande = qtdLatas[2] * PRECO_LTS_GRANDE;
    valorLtsRestoPequena = qtdLatas[3] * PRECO_LTS_PEQUENA;
    a = [qtdLatas[0], math.floor(valorLtsGrade)];
    b = [qtdLatas[1], math.floor(valorLtsPequena)];
    c = [qtdLatas[2], math.floor(valorLtsRestoGrande)];
    c2 = [qtdLatas[3], math.floor(valorLtsRestoPequena)];
    return [a, b, c, c2];

def processaValor():
    area = float(input());
    valor_final = calcValorFinal(area);
    print('a) {0} latas(s) de 24 litros: R$ {1:.2f}'.format(valor_final[0][0], valor_final[0][1]));
    print('b) {0} latas(s) de 5.4 litros: R$ {1:.2f}'.format(valor_final[1][0], valor_final[1][1]));
    print('c) {0} latas(s) de 24 litros e {1} lata(s) de 5.4 litros: R$ {2:.2f}'.format(valor_final[2][0], valor_final[3][0], (valor_final[2][1] + valor_final[3][1])));

processaValor()

