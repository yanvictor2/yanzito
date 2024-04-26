# import time

# import emoji

# # for f in range(10,0,-1):
# #   print(f)
# #   time.sleep (1)
# # print('estouro dos fogos artificiais')
# soma = 0
# for impar in range(1, 500, 2):
#   if impar % 3 == 0:
#       print(impar)
#   soma = soma + impar
# print(soma)
# tabu = int(input('digite um numero para ver sua tabuada: '))
# for tabuada in range(0, 101):
#   produto = tabu * tabuada
#   print(f'{tabu} * {tabuada} = {produto}')
soma_pares = 0

for i in range(6):
    s = int(input('digite um numero: '))
    if s % 2 == 0:
        soma_pares = s + soma_pares
print(f'a soma dos numeros pares e {soma_pares} ')
