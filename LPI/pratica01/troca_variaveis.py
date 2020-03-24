#Complete o código do programa em Python3 que recebe dois valores quaisquer, armazenando-os nas variáveis v1 e v2, e em seguida troca os valores de v1 e v2 e imprime os valores trocados.

v1 = input("digite o valor 1:");
v2 = input("digite o valor 2:");

aux = v2;
v2 = v1;
v1 = aux;

print('valor em v1:', v1);
print('valor em v2:', v2);