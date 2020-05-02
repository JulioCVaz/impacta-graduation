# Crie um programa que tenha uma única função, além da principal, que receberá como parâmetro uma string não vazia s (com no máximo 50 caracteres de conteúdo) e exibirá a quantidade de caracteres de s. Observações: (a) apenas um laço de repetição; (b) sem matrizes auxiliares; (c) não usar funções prontas; (d) função iterativa.


def countLenString(string):
    count = 0
    for char in string:
        if count == 50:
            break
        count += 1
    return count


def main():
    s = input()
    return print(countLenString(s))


main()
