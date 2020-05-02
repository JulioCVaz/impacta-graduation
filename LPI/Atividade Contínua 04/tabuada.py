def calcTabuada(number):
    res = []
    size = 10

    for i in range(size):
        if i < 10:
            res.append(number * (i + 1))
    return res


def main():
    number = int(input())
    tabuada = calcTabuada(number)
    return print(f'{number} X 1 = {tabuada[0]}\n{number} X 2 = {tabuada[1]}\n{number} X 3 = {tabuada[2]}\n{number} X 4 = {tabuada[3]}\n{number} X 5 = {tabuada[4]}\n{number} X 6 = {tabuada[5]}\n{number} X 7 = {tabuada[6]}\n{number} X 8 = {tabuada[7]}\n{number} X 9 = {tabuada[8]}\n')


main()
