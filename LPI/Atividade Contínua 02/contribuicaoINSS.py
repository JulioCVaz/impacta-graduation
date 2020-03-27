# Na empresa em que você trabalha há muitos funcionários, e às vezes o depósito do INSS é feito incorretamente para alguns deles pois é um processo manual e portanto sujeito a erros. Com isso você decidiu propor a automação de tal processo, para torná-lo mais rápido e reduzir a chance de erros. Escreva um programa que receba o salário base de um funcionário e calcule qual a contribuição devida ao INSS, dada de acordo com a seguinte tabela:


salario = float(input());

ALIQUOTA_8 = 0.08;
ALIQUOTA_9 = 0.09;
ALIQUOTA_11 = 0.11;
SALARIO_TETO = 5839.45;

if salario <= 1751.81:
    desconto = salario * ALIQUOTA_8;
elif salario >= 1751.82 and salario <= 2919.72:
    desconto = salario * ALIQUOTA_9;
elif salario >= 2919.73 and salario <= SALARIO_TETO:
    desconto = salario * ALIQUOTA_11;
else:
    desconto = SALARIO_TETO * ALIQUOTA_11;

print('Desconto do INSS: R$ {0:.2f}'.format(desconto));