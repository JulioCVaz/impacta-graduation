#Escreva um programa em Python3 que receba a altura de 4 pessoas, calcule e imprima a média final.
def calculaMediaSimples(pesos):
    soma = sum(pesos);
    return float(soma / len(pesos)) 

def pegaPeso():
    pesos = [];
    for x in range (4):
        peso = float(input(f'Pessoa {x + 1} Digite o seu peso: '));
        pesos.append(peso);
    return calculaMediaSimples(pesos)
    
print(pegaPeso());