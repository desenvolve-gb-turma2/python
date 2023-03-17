# -*- coding: utf-8 -*-
"""Desafio01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MzYqCYIbFLT2hQ4vF6blSZbwSBu8lgcN

Notebook: Igor R Amorim

# Contextualização:

João quer montar um painel de leds contendo diversos números. 
Ele não possui muitos leds, e não tem certeza se conseguirá montar o número desejado. 

Considerando a configuração dos leds dos números abaixo, faça um algoritmo que ajude João a descobrir a quantidade de leds necessário para montar o valor.

![image.png](data:image/png;base64,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)

Entrada
- A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste, seguido de N linhas, cada linha contendo um número (1 ≤ V ≤ 10^100) correspondente ao valor que João quer montar com os leds.

Saída
- Para cada caso de teste, imprima uma linha contendo o número de leds que João precisa para montar o valor desejado, seguido da palavra "leds".

# Bibliotecas Utilizadas
"""

#biblioteca utilizada para limpar o terminal
from IPython.core.display import clear_output

"""# Funçoes do Programa"""

def leiaInt(msg = ''):  # inserido após decidir colocar a opção desejada pelo cliente
    while True:  # lendo até ser correto
        try:
            n = input(msg)
            n = int(n)
        except (ValueError, TypeError):
            print('\033[31m', 'ERRO!', '\033[0;0m', f'O Valor {n} não é um número valido' )
            print('Por favor, digite um valor válido.')
            continue
        else:
            return n
            
def menu(lista, titulo):
  opc = 0
  while True:
    print('-'*50)
    print(titulo.center(50))  # certo da quantidade de caracteres
    print('-'*50)

    # para não ficar como lista, criar um contador:
    for i, item in enumerate(lista, start=1):
        print(f'\033[34m', i, '\033[0;0m', '-','\033[1;36m', item,'\033[0;0m')

    print() 
    opc = leiaInt('Sua Opção: ')
      
    if (opc-1 >= len(lista) or opc <= 0):
      clear_output(wait=True)
      print('\033[31m', 'ERRO!'+'\033[0;0m', f'O Valor {opc} não é uma opção válida' )
      print(' Por favor, tecle um valor dentro das opções.\n')
    else:
      clear_output(wait=True)
      print(f'A opção escolhida foi: {opc} - {lista[opc-1]}')
      break
  return opc

tabela_leds={
    '1':2,
    '2':5,
    '3':5,
    '4':4,
    '5':5,
    '6':6,
    '7':3,
    '8':7,
    '9':6,
    '0':6
}

quadro1 = ['Sair', 'Escolher um novo numero']
while True:
  opcao = menu(quadro1, "Contador de leds")
  if opcao == 1:
    break
  
  elif opcao == 2:
    print('\nInsira o numero desejado para calcular a quantidade de leds')
    N = leiaInt()
    if N < (10**100):
      lista = list(str(N))
      print('\nCalculando...')
      V = 0
      for i in lista:
        V += tabela_leds.get(i)
      print('Resultado:', V,'Leds')
    else:
      print('\033[31m', 'ERRO!', '\033[0;0m', f'O Valor {N} não é um valor valido' )
      print('Por favor, escolha novamente um numero válido.')
