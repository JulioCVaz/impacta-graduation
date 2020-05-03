# Atividade contínua 04 - Lógica de Programação
# Aluno: Júlio César de O.Vaz - 1903201 - ADS EAD - Turma A
# Prof: Andreia Cristina


def main():

    #a) Peça para o usuário digitar a quantidade de nomes que irá digitar e armazene na variável n. Essa variável n deverá ser maior que 3 e menor que 10 (Validação de dados de entrada). O armazenamento da variável n deverá ser feito em uma lista "l".
  n = int(input('Quantos nomes você irá digitar? (Exe: 1,2,3...): '));

  if(n < 3):
    print('O mínimo são 4 nomes...\n');
    n = int(input('Digite a quantidade de nomes novamente:'))
  
  if(n > 10):
    print('O máximo são 9 nomes...\n');
    n = int(input('Digite a quantidade de nomes novamente: '))
  
  count = 0;
  nomes = [];

  while(count < n) :
    nome = input('Digite o {0} nome: '.format((count + 1)));
    nomes.append(nome)
    count += 1

 #1º) Adiciona o nome "Teste" no índice 3 (estava escrito "posição 3").
  nomes.insert(3, 'Teste')

 #2º) Exclua o elemento de índice 2.
  del nomes[2]

#3º) Verifique quantas vezes você digitou o nome 'Ana'. Se for maior que 0, mostre o índice da primeira ocorrência. Se for 0, mostre uma frase informando que o nome Ana não existe na lista.
  anas = []

  for i in range(len(nomes)):
    if(nomes[i] == 'Ana'):
      anas.append(i)

  if (len(anas) > 0):
    print('A primeira ocorrência do nome Ana encontra-se na posiçao {0} da lista'.format(anas[0]))
  else:
    print('O nome Ana não existe na lista')

    #4º) No final, mostre a lista ordenada.

  print('Lista de nomes desordenada: {0}'.format(nomes));
  
  nomes.sort()

  print('Lista de nomes ordenada: {0}'.format(nomes));

main()