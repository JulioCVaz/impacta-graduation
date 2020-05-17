# Dada uma lista de compras, queremos saber qual é o item mais caro da lista.
# Uma sequência de itens, cada um descrito numa linha. Cada item contém um código de produto (um número inteiro), a quantidade do produto e o preço unitário (um float).

# A sequência termina com um item com 0 como código do produto. Este último item não deve ser considerado para o cálculo.


def main():
    products = []
    most_expensive = []

    while True:
        product = input()
        splited = product.split()

        if int(splited[0]) == 0 and len(products) == 0:
            print('nao tem compras')
            break
        elif int(splited[0]) == 0 and len(product) > 0:
            for i in products:
                prod = i.split()
                calc = int(prod[1]) * float(prod[2])
                if len(most_expensive) > 0:
                    if most_expensive[2] < calc:
                        most_expensive = [int(prod[0]), int(prod[1]), calc]
                else:
                    most_expensive = [int(prod[0]), int(prod[1]), calc]
            print(
                f"Item mais caro\nCodigo: {most_expensive[0]}\nQuantidade: {most_expensive[1]}\nCusto: {most_expensive[2]:.2f}")
            break
        else:
            products.append(product)


main()
