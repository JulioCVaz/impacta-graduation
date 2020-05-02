def calcTabuadas(n1, n2):
    for i in range(n1, (n2 + 1)):
        for j in range(1, 10):
            print(f'{i} x {j} = {i * j}')
        print()


def main():
    n1 = int(input())

    # validation
    while(n1 < 1 or n1 > 9):
        print('Insira um número inicial entre 1 e 9')
        n1 = int(input())

    n2 = int(input())

    while(n2 < 1 or n2 > 9):
        print('Insira um número final entre 1 e 9')
        n2 = int(input())

    if n1 > n2:
        return print('Nenhuma tabuada nesse intervalo')

    return calcTabuadas(n1, n2)


main()
