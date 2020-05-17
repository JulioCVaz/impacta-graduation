# O objetivo desse problema é a implementação de funções que indiquem se um determinado ano é ou não bissexto.

# Para cada ano fornecido ao programa, faz-se necessário, primeiro, identificar se o ano fornecido é um valor inteiro de 4 dígitos e, segundo, dado que o ano é um número válido, informar se é ou não um ano bissexto.

# Um ano é bissexto se ele satisfaz as seguintes condições:

# É divisível por 4 e,
# Não é divisível por 100 ou é divisível por 400.
# A sua tarefa é construir uma solução com três funções (3): contaDigitos, ehBissexto e Mensagem.

import datetime


def ehBissexto(year):
    now = datetime.datetime.now()
    if year % 4 == 0 and ((not year % 100 == 0) or year % 400 == 0) and year >= now.year:
        Mensagem(f'O ano {year} serah bissexto')
    elif year % 4 == 0 and ((not year % 100) == 0 or year % 400 == 0) and year < now.year:
        Mensagem(f'O ano {year} foi bissexto')
    else:
        Mensagem(f'O ano {year} NAO eh bissexto')
    return


def Mensagem(string):
    print(string)


def contaDigitos(year):
    if len(year) == 4:
        ehBissexto(int(year))
    else:
        Mensagem('Ano invalido')
    return


def main():
    years = input()
    for i in years.split():
        contaDigitos(i)


main()
