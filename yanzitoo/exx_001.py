# Atribuição de Valores Simples: Declare uma variável chamada idade e atribua a ela sua idade atual. Em seguida, imprima essa variável na tela.
#################################################################################################################
# idade = 10
# print(idade)
#################################################################################################################
# Operações com Variáveis: Declare duas variáveis, a e b, atribua a elas valores numéricos e em seguida, calcule a soma, a diferença, o produto e o quociente desses va lores.
#################################################################################################################
# a = 177
# b = 187
# soma = a+b
# diferenca = a-b
# produto = a*b
# quociente = a/b
# print(f'a soma e {soma} a diferença e {diferenca} o produto e {produto} e o quociiente e { quociente} ')
#################################################################################################################
# Variáveis de Texto: Declare uma variável chamada nome e atribua a ela seu primeiro nome. Em seguida, imprima uma mensagem de boas-vindas utilizando essa variável.
#################################################################################################################
# nome = 'yan'
# print(f'bem vindo {nome}')

#################################################################################################################
# Interatividade: Crie um programa onde o usuário possa inserir o seu nome. Armazene este nome em uma variável e, em seguida, imprima uma mensagem personalizada de boas-vindas usando essa variável.
#################################################################################################################
# nome = str(input('digite seu nome: '))
# print(f'\033[1;34;44mbem vindo {nome} \033[m')
#################################################################################################################
# Jogo de Escolhas: Crie um jogo simples de pedra, papel e tesoura, onde o jogador e o computador fazem uma escolha (pedra, papel ou tesoura) e armazenam essas escolhas em variáveis. Depois, compare as escolhas e determine o vencedor do jogo.
#################################################################################################################
# Calculadora Simples: Crie um programa que solicita ao usuário que insira dois números e, em seguida, exibe a soma, subtração, multiplicação e divisão desses números.
#################################################################################################################
# a = float(input('digite um  numero: '))
# b = float(input('digite outro numero: '))
# soma = a+b
# diferenca = a-b
# produto = a*b
# quociente = a/b
# print(f'a soma e {soma} a diferença e {diferenca} o produto e {produto} e o quociiente e { quociente} ')
#################################################################################################################
# Conversor de Temperatura: Faça um programa que pergunte ao usuário a temperatura em graus Celsius e converta para Fahrenheit, exibindo o resultado na tela.
#################################################################################################################
#################################################################################################################
# Verificador de Maioridade: Escreva um programa que pede ao usuário sua idade e informa se ele é maior de idade ou não.
#################################################################################################################
# idade = int(input('digite sua idade: '))
# if  idade >=18:
#   print('vocë e maior de idade')
# else:
#   print('você nao e maior de idade')

#################################################################################################################
# Calculadora de IMC: Crie um programa que solicite ao usuário seu peso (em kg) e altura (em metros) e, em seguida, calcule e exiba o Índice de Massa Corporal (IMC).
#################################################################################################################
# kg = float(input('quantos kg voce tem? '))
# metros = float(input('quntos metros voce tem? '))
# imc = kg/metros
# print(f'o  seu imc e igual a {imc:.2f}')
#################################################################################################################
# Jogo de Adivinhação: Desenvolva um jogo em que o programa escolhe um número aleatório entre 1 e 100 e o jogador precisa adivinhar qual é esse número.
# O programa deve fornecer dicas se o palpite do jogador for muito alto ou muito baixo.
#################################################################################################################
# import random
# print('-='*30)
# print('Sou seu COMPUTADOR e estou pensando em um numero entre 0 e 100. tente advinhar...')
# print('-='*30)
# numeros_que_o_pc_esta_pensando = random.randint(0, 100)
# while True:
#     advinhe = int(input('digite o numero que voce acha que estou pensando: '))

#     if advinhe == numeros_que_o_pc_esta_pensando:
#         print('parabens voce ganhou: )')
#     else:

#         print(
#             f'o numero que eu pensei esta entre {numeros_que_o_pc_esta_pensando - 5} e {numeros_que_o_pc_esta_pensando + 5}')

#################################################################################################################
# Comparação de Idades: Escreva um programa que peça a idade de dois usuários e determine qual deles é mais velho.
#################################################################################################################
# idade_1 = int(input('digite a idade do seu mior amigo: '))
# idade_2 = int(input('digite sua idade: '))
# if idade_1 > idade_2:
#     print('seu amigo e mais velho')
# elif idade_1 == idade_2:
#   print('voces dois tem a mesma idade')
# else:
#   print ('voce e mais velho')
# Verificação de Aprovação: Solicite ao usuário que insira sua nota em um exame e defina um ponto de corte. O programa deve determinar se o aluno passou ou não no exame, exibindo uma mensagem correspondente.
# nota = float(input('digite sua nota'))
# if nota >= 7:
#     print('voce passou')
# else:
#     print('voce reprovou mas voce deu vaga para outra pessoa')

#################################################################################################################
# Jogo de Adivinhação: Modifique o jogo de adivinhação anterior (exercício de entrada e saída) para incluir a comparação do palpite do jogador com o número
# secreto, utilizando operadores de comparação.
#################################################################################################################
# import random
# print('-='*30)
# print('Sou seu COMPUTADOR e estou pensando em um numero entre 0 e 100. tente advinhar...')
# print('-='*30)
# numeros_que_o_pc_esta_pensando = random.randint(0, 100)
# while True:
#     advinhe = int(input('digite o numero que voce acha que estou pensando: '))

#     if advinhe == numeros_que_o_pc_esta_pensando:
#         print('parabens voce ganhou: )')
#     else:

#         print(
#             f'o numero que eu pensei esta entre {numeros_que_o_pc_esta_pensando - 5} e {numeros_que_o_pc_esta_pensando + 5}')
#         print(f' o numero que o computador pensou enta entre {random.}')
#################################################################################################################
# Ordenação de Números: Peça ao usuário que insira três números e exiba-os em ordem crescente.
#################################################################################################################
# a = int(input('digite um valor: '))
# b = int(input('digite outro valor: '))
# c = int(input('digite mais um valor: '))
# if a > b and a > c and b > c:
#     print(f'o numero {a} > {b} > {c}')
# elif a < b and a > c and b > c:
#     print(f'o numero {b} > {a} > {c}')
# elif c
#################################################################################################################
# Classificação de Idade: Crie um programa que pergunte ao usuário sua idade e, com base nessa idade, classifique-o em uma das seguintes categorias:
# bebê, criança, adolescente, adulto jovem, adulto ou idoso.
#################################################################################################################
# idade = int(input('digite sua idade: '))
# if idade <= 3:
#   print('voce e um bebe')
# elif idade  <= 12:
#  print('voce e uma criança')
# elif idade <=18:
#   print('voce e um adolescente')
# elif idade <=24:
#   print('voce e jovem')
# elif idade <= 60:
#   print('voce e adulto')
# else:
#   print('voce e um idoso')


#################################################################################################################
# Verificação de Paridade: Peça ao usuário para inserir um número e informe se ele é par ou ímpar.
#################################################################################################################
# n = int(input('digite um numero'))
# resto = n % 2
# if resto == 0:
#   print('o seu numero e par :)')
# else:
#   print('o seu numero e impar')
#################################################################################################################
# Decisão de Jogo: Crie um programa que simula uma decisão em um jogo. Pergunte ao jogador se ele quer abrir a porta 1, 2 ou 3. Em seguida, informe o
# resultado com base na escolha.
#################################################################################################################
# import random

# escolha = int(input('digite um das portas ->>> 1,2 ou 3: '))
# escolha_do_pc = random.randint(1,3)
# if escolha == escolha_do_pc:
#   print(' voce acertou a porta')
# else:
#   print('franguinho voce errou a porta ')
# #################################################################################################################
# Solicite ao usuário que insira sua nota e, com base nessa nota, exiba sua classificação (A, B, C, D ou F).
#################################################################################################################
#################################################################################################################
# Verificação de Login: Crie um programa que solicite ao usuário que insira seu nome de usuário e senha. Verifique se ambos estão corretos e exiba uma mensagem de login bem-sucedido ou falha de autenticação.

#################################################################################################################
# Comparação de Idades: Peça a idade de dois usuários e informe qual deles é mais velho, mais novo ou se têm a mesma idade.

#############################################################################################################
# Contagem Crescente: Escreva um programa que imprima os números de 1 a 10.

#############################################################################################################
# Tabuada de Multiplicação: Crie um programa que solicite ao usuário um número e imprima a tabuada de multiplicação desse número de 1 a 10.

#############################################################################################################
n = int(input('digite qual tabuada voce quer ver'))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
print(15*"=")
print(f' A TABUADA DE {n}:')
print(15*"=")
print(f'{n} * 1 ={n1}')
print(f'{n} * 2 = {n2}')
print(f'{n} * 3 = {n3}')
print(f'{n} * 4 = {n4}')
print(f'{n} * 5 = {n5}')
print(f'{n} * 6 = {n6}')
print(f'{n} * 7 = {n7}')
print(f'{n} * 8 = {n8}')
print(f'{n} * 9 = {n9}')
print(f'{n} * 10 = {n10}')
print(15*"=")

# Soma dos Números Pares: Escreva um programa que calcule e imprima a soma dos números pares de 1 a 100.

#############################################################################################################
# Lista de Compras: Crie um programa que peça ao usuário para inserir cinco itens de uma lista de compras e, em seguida, imprima cada item.

#############################################################################################################
# Tabuada Personalizada: Faça um programa que peça ao usuário um número e, em seguida, imprima a tabuada de multiplicação desse número de 1 a 10, mas apenas os resultados ímpares.

#############################################################################################################
