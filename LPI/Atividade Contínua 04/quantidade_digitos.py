def countLenNumber(number):
    count = 0
    for n in str(number):
        count += 1
    return count


def main():
    n = int(input())
    return print(countLenNumber(n))


main()
