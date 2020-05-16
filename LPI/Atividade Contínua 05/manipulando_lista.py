# Escreva um programa que permita manipular uma lista de inteiros. Inicialmente o programa deve ler os inteiros separados por espaço em branco e armazenar em uma lista. Dado que os valores inteiros estão armazenados, o programa deve aceitar 4 comandos: inserir, remover, parcial e final. O comando inserir é acompanhado na mesma linha do valor inteiro a ser inserido na lista. Da mesma forma, o comando remover é acompanhado do valor a ser removido da lista. Já o comando parcial deve fazer com que os dados contidos na lista sejam impressos na tela, separados por espaços em branco e dispostos em ordem crescente(numérica). O mesmo deve fazer o comando final, exceto que este encerra a execução do programa.


def main():
    # recebe valores
    values = input().split()
    numbers = []
    for i in values:
        if i != ' ':
            numbers.append(i)

    while(True):
        command = input()

        # if command == inserir
    # controi comandos


main()
