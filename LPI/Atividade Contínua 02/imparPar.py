# Você deve pedir que o usuário entre com um número inteiro, e deverá dizer se ele eh impar ou se ele eh par:
# Se ele for par imprima "O numero eh N e ele eh par"
# Se ele for impar imprima "O numero eh N e ele eh impar"
# Onde N eh o numero digitado pelo usuário


def checkSeEhImparPar(n):
    if(n % 2 == 0):
        print(f'O numero eh {n} e ele eh par');
    else:
        print(f'O numero eh {n} e ele eh impar');

def recebeValores():
    n = int(input());
    return checkSeEhImparPar(n);

recebeValores();