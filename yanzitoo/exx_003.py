nome = str (input('digite seu nome: '))
idade = int (input('digite sua idade: '))
print(f'seu nome e {nome}')
print(f'seu nome invertido e {nome[::-1]}')
if ' ' in nome:
  print (f'o nome {nome} tem espaços')
else:
  print(f'o nome nao tem espaços')
print(f'o seu nome tem {len(nome)} letras')
print(f'a primeira letra do seu nome e {nome[0]}')
print(f'a ultima letra do seu nome e {nome[-1]}')