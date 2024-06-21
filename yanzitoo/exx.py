"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# NUMERO_1 = int(input('digite um numero: '))
# if (NUMERO_1 % 2 ) == 0:
#   print(f'o numero {NUMERO_1} e par')
# else:
#   print(f'o numero {NUMERO_1} e impar')
# print('fim')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario = int(input('digite o horario que voce esta: '))
# if horario < 12 :
#   print('bom dia')
# elif horario < 18 :
#   print ('boa tarde')
# else:
#   print('boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = (input('digite seu nome: '))
# nome_numero = len(nome)
# if nome_numero < 5:
#   print('seu nome e considerado curto')
# elif nome_numero <7:
#   print('o seu nome e considerado medio')
# else:
#   print('seu nome e considerado grande')

"""Exercício 1: Flags
Descrição: Crie um programa que simule o processo de verificação de presença em uma 
lista de convidados. Utilize uma flag para indicar se um convidado específico foi encontrado."""

convidados = {'yan','silas','sara','ana','erivan'}
nome_dos_convidados = (input('digite o nome da falta: '))
encontrado = False
for nomes in convidados:
  if nomes == nome_dos_convidados:
    encontrado = True
if encontrado:
  print('convidado encontrado')
else:
  print('convidado nao encontrado')