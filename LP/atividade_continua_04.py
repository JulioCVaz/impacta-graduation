


def main():
  n = int(input('Quantos nomes você irá digitar? (Exe: 1,2,3...)'));

  if(n < 3):
    print('O mínimo são 4 nomes...');
    n = int(input('Digite a quantidade de nomes novamente:'))
  
  if(n > 10):
    print('O máximo são 9 nomes....');
    n = int(input('Digite a quantidade de nomes novamente: '))
  
  count = 0;
  nomes = [];

  while(count < n) :
    nome = input('Digite o nome: ');
    nomes.append(nome)
    count += 1

  nomes.insert(3, 'Teste')

  del nomes[2]

  anas = []

  print(nomes)

  for i in range(len(nomes)):
    if(nomes[i] == 'Ana'):
      anas.append(i)

  if (len(anas) > 0):
    print('Ana na posiçao {0}'.format(anas[0]))
  else:
    print('O nome Ana não existe na lista')

  nomes.sort()

  print(nomes)

main()