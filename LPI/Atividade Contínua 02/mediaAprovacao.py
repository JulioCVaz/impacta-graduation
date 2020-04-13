# Escreva um programa que receba as notas e a presença de um aluno, calcule a média e imprima a situação final do aluno.
# No semestre são feitas 3 provas, p1, p2 e p3, e faz-se a média ponderada com pesos 2, 2 e 3, respectivamente.
# Os critérios para aprovação são:
# 1 - Frequência mínima de 75%.
# 2 - Média final mínina de 6.0 (calculada com uma casa de precisão).
# E devem ser considerados os casos especiais descritos para a impressão dos resultados, com uma mensagem personalizada para cada situação.

import math

PESOP1 = 2;
PESOP2 = 2;
PESOP3 = 3;

def calcMediaPonderada():
    nota1 = float(input());
    nota2 = float(input());
    nota3 = float(input());
    result = ((nota1 * PESOP1) + (nota2 * PESOP2) + (nota3 * PESOP3 )) / sum([PESOP1, PESOP2, PESOP3]);
    return round(result, 1);

def calcFrequencia():
    frequencia = float(input());
    result = frequencia * 100;
    return result;

def init():
    mediaFinal = calcMediaPonderada();
    frequenciaFinal = calcFrequencia();
    mensagem = "";

    if frequenciaFinal < 75:
        print('Frequencia: {0:.0f}%\nMedia: {1:.1f}\nAluno reprovado por faltas!'.format(frequenciaFinal, mediaFinal));
    elif frequenciaFinal >= 75 and mediaFinal > 9:
        print('Frequencia: {0:.0f}%\nMedia: {1:.1f}\nAluno aprovado com louvor!'.format(frequenciaFinal, mediaFinal));
    elif frequenciaFinal >= 75 and mediaFinal >= 6 and mediaFinal <= 9:
        print('Frequencia: {0:.0f}%\nMedia: {1:.1f}\nAluno aprovado!'.format(frequenciaFinal, mediaFinal));
    elif frequenciaFinal >= 75 and mediaFinal >= 4 and mediaFinal < 6:
        print('Frequencia: {0:.0f}%\nMedia: {1:.1f}\nAluno de recuperação!'.format(frequenciaFinal, mediaFinal));
    else:
        print('Frequencia: {0:.0f}%\nMedia: {1:.1f}\nAluno reprovado!'.format(frequenciaFinal, mediaFinal));

init();


