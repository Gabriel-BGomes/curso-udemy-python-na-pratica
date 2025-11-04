#Faça um programa que recebe um número inteiro do usuário e calcule o fatorial deste número.

#Dica: utilize o módulo math do Python, especificamente math.fatorial.

import math
num=int(input('Digite um número inteiro: '))
fatorial=math.factorial(num)
print(f'O fatorial de {num} é {fatorial}')