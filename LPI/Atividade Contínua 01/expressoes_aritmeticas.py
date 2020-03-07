#Escreva um programa em Python3 que receba quatro números reais (a, b, c, d) e reproduza as seguintes expressões algébricas: 

import math;

def primeiraExpressao(valores):
    return round(((valores[0] ** 2 + (3 * valores[1])) / valores[2]) + valores[3], 4);

def segundaExpressao(valores):
    return round(math.log(valores[0], 10) + (math.e ** (-(valores[1] / valores[2]))) - ((valores[3] ** 2) / math.pi), 4);

def terceiraExpressao(valores):
    return round((((valores[0] ** 2) ** (1./3.) * (valores[1] ** (1/3))) + (valores[2] * valores[3])) / sum(valores), 4);

def testaExpressoes(exp, arr):
    for x in range(len(arr)):
        print(exp(arr[x]));

def recebeValores():
    valores = [2.5,1.7,0.3,5.4];
    valores1 = [2, 4, -3, -1];
    valores2 = [25, 364, 125, 687];
    # for x in range (4):
    #     valores.append(float(input()))
    
    primeiraExp = primeiraExpressao(valores);
    segundaExp = segundaExpressao(valores);
    terceiraExp = terceiraExpressao(valores);

    return testaExpressoes(terceiraExpressao, [valores, valores1, valores2]);

    # print(terceiraExp);

recebeValores();