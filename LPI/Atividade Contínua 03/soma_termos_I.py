# Escreva um programa em Python 3 para somar os n primeiros termos da seguinte série:

# DICA: Aqui todas as frações são somadas, mas como calcular o denominador? Tente primeiro fazer a exibição apenas dos denominadores.

# Os denominaores são: 1, 4, 9, 16, 25, 36, .... qual a relação entre eles e a posição dos números?

# Compare com a posição: 1, 2, 3, 4, 5, 6, ....

n = int(input())
impar = 1;
denominador = 1;

count = 0;
nums = 0;

razao = 0;

while(n):
    nums += ((1/denominador))

    impar += 2
    razao = denominador + impar
    denominador = razao
    
    n -= 1;

print(f'{nums:.6f}')