#A companhia aérea Easy Jet oferece passagens baratas para várias cidades européias e é muito procurada por turistas de todo o mundo. Entretanto, ela tem regras muito rígidas para o tamanho da bagagem de mão de cada cliente: para ser aceita, a mala deve ter no máximo 45 cm de largura, 56 cm de comprimento e 25 cm de altura.
#Escreva um programa que receba como entrada as dimensões de uma mala e exiba uma mensagem informando se a mala será aceita ou não.

MENSAGEM_PERMITIDA = 'PERMITIDA';
MENSAGEM_PROIBIDA = 'PROIBIDA';
LARGURA = 45;
COMPRIMENTO = 56;
ALTURA = 25;

def checkDimensoesMala(dimensoes):
    if dimensoes[0] <= LARGURA and dimensoes[1] <= COMPRIMENTO and dimensoes[2] <= ALTURA:
        return print(MENSAGEM_PERMITIDA);
    else :
        return print(MENSAGEM_PROIBIDA);

def recebeValores():
    dimensoes = [];

    for x in range(3):
        dimensoes.append(float(input("")));

    return checkDimensoesMala(dimensoes)

recebeValores();