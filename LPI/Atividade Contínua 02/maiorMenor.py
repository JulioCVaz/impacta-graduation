# Dados dois números inteiros A e B, exibir:
# - 'A eh maior', se A for maior do que B;
# - 'B eh maior', se B for maior do que A;
# - 'iguais', se os números forem iguais.


def checkAmaiorB(valores):
    if valores[0] > valores [1]:
        print('A eh maior');
    elif valores[0] < valores [1]:
        print('B eh maior');
    else:
        print('iguais');

def recebeValores():
    valores = [];
    for x in range(2):
        valores.append(int(input("")));

    return checkAmaiorB(valores)

recebeValores();