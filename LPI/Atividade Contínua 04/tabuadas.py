def calcTabuadas(n1, n2):
    tabuadas = []
    size = n2
    if n1 > 0 & n2 < 10:
        if(n1 == n2):
            size = 1
        for i in range(size):
            for j in range(8):
                tabuadas[i] = 2

    return 0


def main():
    n1 = int(input())
    n2 = int(input())
    tabuadas = calcTabuadas(n1, n2)


main()
