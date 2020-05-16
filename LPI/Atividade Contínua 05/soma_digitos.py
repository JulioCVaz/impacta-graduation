# Crie um programa que tenha uma única função, além da principal, que receberá como parâmetro um natural n (0<=n<=2^30) e devolverá a soma dos dígitos de n. O programa exibirá o retorno da função. Observações: (a) apenas um laço de repetição; (b) sem matrizes; (c) função iterativa.


def sumNumbers(number):
    count = 0
    for i in str(number):
        count += int(i)
    return count


def main():
    n = int(input())
    print(sumNumbers(n))


main()
