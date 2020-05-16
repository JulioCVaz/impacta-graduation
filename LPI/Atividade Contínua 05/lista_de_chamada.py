# Tia Joana é uma respeitada professora e tem vários alunos. Em sua última aula, ela prometeu que iria sortear um aluno para ganhar um bônus especial na nota final: ela colocou N pedaços de papel numerados de 1 a N em um saquinho e sorteou um determinado número K; o aluno premiado foi o K-ésimo aluno na lista de chamada.
# O problema é que a Tia Joana esqueceu o diário de classe, então ela não tem como saber qual número corresponde a qual aluno. Ela sabe os nomes de todos os alunos, e que os números deles, de 1 até N, são atribuídos de acordo com a ordem alfabética, mas os alunos dela estão muito ansiosos e querem logo saber quem foi o vencedor.
# Dado os nomes dos alunos da Tia Joana e o número sorteado, determine o nome do aluno que deve receber o bônus.


# sort no array
# o primeiro nome da lista é o premiado

def main():
    values = input().split()
    n = int(values[0])
    k = int(values[1])

    names = []

    for i in range(n):
        name = input()

        if not name.isdigit():
            if len(name) >= 1 and len(name) <= 20:
                names.append(name)

    names.sort()
    print(names[k - 1])


main()
