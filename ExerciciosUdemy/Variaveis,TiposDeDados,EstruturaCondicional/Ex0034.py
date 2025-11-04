#Modifique o programa anterior e permita que o usuário especifique o ano e o mês a serem mostrados na tela.

import calendar
mes = int(input(f'Digite o mes que você deseja: '))
ano = int(input(f'Digite o ano que você deseja: '))

print(calendar.month(ano, mes))