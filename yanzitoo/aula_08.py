# import random

# alunos=random.randint(0,3)
# if alunos == 0:
#   print('o aluno pedro vai apagar o quadro')
# elif alunos ==1:
#   print('a aluna anna bella vai apagar o quadro')
# elif alunos ==2:
#   print('o aluno icaro vai apagar o quadro')
# elif alunos ==3:
#   print('a aluna lays vai apagar o quadro')


# import random

# frutas=['banana','maça','laranja','abacate','pera']
# frutas_escolhidas=random.choice(frutas)
# print (f'a fruta escolhida para hoje e {frutas_escolhidas}: )')


import random

x=0

while x<5:
  opções = ['pedra', 'papel', 'tesoura']
  escolha_do_pc = random.choice(opções)
  minha_escolha = str(input('Digite entre: pedra, papel ou tesoura: '))
  if escolha_do_pc == 'pedra' and minha_escolha == 'pedra':
      print('O jogo empatou')
  if escolha_do_pc == 'pedra' and minha_escolha == 'papel':
      print('vc ganhou')
  if escolha_do_pc == 'pedra' and minha_escolha == 'tesoura':
      print('vc perdeu')
  if escolha_do_pc == 'papel' and minha_escolha == 'pedra':
      print('vc perdeu')
  if escolha_do_pc == 'papel' and minha_escolha == 'papel':
      print('O jogo empatou')
  if escolha_do_pc == 'papel' and minha_escolha == 'tesoura':
      print('vc ganhou')
  if escolha_do_pc == 'tesoura' and minha_escolha == 'pedra':
      print('vc ganhou')
  if escolha_do_pc == 'tesoura' and minha_escolha == 'papel':
      print('O jogo empatou')
  if escolha_do_pc == 'tesoura' and minha_escolha == 'tesoura':
      print('O jogo empatou')
  x=x+1