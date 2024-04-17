import math
import emoji

n = float(input('digite um numero: '))
n1 = math.sqrt(n)
print(f'a raiz quadrada de {n} e igual a {n1:.2f}')
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))