
from fractions import Fraction

n = int(input())
impar = 1;
denominador = 1;

count = 0;
nums = [];

razao = 0;

while(n):
    nums.append(Fraction(1, denominador))

    impar += 2
    razao = denominador + impar
    denominador = razao
    
    n -= 1;

soma = sum(nums)
result = soma.numerator / soma.denominator

print(f'{result:.6f}')