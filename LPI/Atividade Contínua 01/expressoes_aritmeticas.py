#Escreva um programa em Python3 que receba quatro números reais (a, b, c, d) e reproduza as seguintes expressões algébricas: 

import math;

def primeiraExpressao(valores):
    return round(((valores[0] ** 2 + (3 * valores[1])) / valores[2]) + valores[3], 4);

def segundaExpressao(valores):
    return round(math.log(valores[0], 10) + (math.e ** ((-(valores[1])) / valores[2])) - ((valores[3] ** 2) / math.pi), 4);

def terceiraExpressao(valores):
    return round((((valores[0] ** 2) ** (1./3.) * (valores[1] ** (1/3))) + (valores[2] * valores[3])) / sum(valores), 4);

def quartaExpressao(valores):
    # ver como funciona o sum e criar uma funcao igual ao sum, mas para multiplicacao
    return round((((valores[0]) + (valores[1])) * ((valores[2]) + (valores[3]))) / ((valores[0]) * (valores[1]) * (valores[2]) * (valores[3])), 4);

def quintaExpressao(valores):
    return round((((valores[0] ** 2) + (valores[1] ** 2)) / ((valores[2]) * (valores[3]))) - (((valores[2] ** 2) + (valores[3] ** 2)) / (valores[0] * (valores[1]))), 4);

def sextaExpressao(valores):
    # verificar como retornar float, esta retornando INT
    return round(sum(valores) ** 2, 4);

def setimaExpressao(valores):
    soma_dos_quadrados = 0;
    for x in range(len(valores)):
        soma_dos_quadrados += ((valores[x]) ** 2);
    return round(soma_dos_quadrados, 4);

def oitavaExpressao(valores):
    return round(((valores[0]) * (valores[1]) * (valores[2]) * (valores[3])) ** (1./3.), 4);

# funcao criada para testar valores mocados
# def testaExpressoes(exp, arr):
#     for x in range(len(arr)):
#         print(exp(arr[x]));

def recebeValores():
    valores = [];
    # valores = [2.5,1.7,0.3,5.4];
    # valores1 = [2, 4, -3, -1];
    # valores2 = [25, 364, 125, 687];
    # testaExpressoes(oitavaExpressao, [valores, valores1, valores2]);

    for x in range (4):
        valores.append(float(input()))
    
    print(f'i) {primeiraExpressao(valores)}\nii) {segundaExpressao(valores)}\niii) {terceiraExpressao(valores)}\niv) {quartaExpressao(valores)}\nv) {quintaExpressao(valores)}\nvi) {sextaExpressao(valores)}\nvii) {setimaExpressao(valores)}\nviii) {oitavaExpressao(valores)}');

recebeValores();

