#Escreva um programa que verifique se um determinado número digitado pelo usuário é nulo, positivo ou negativo.

n = float(input("Digite um número para eu falar se é negativo, positivo ou nulo: "))

if n<0:
    print(f'{n} é negativo')
elif n == 0:
    print(f'{n} é nulo')
else:
    print(f'{n} é positivo')