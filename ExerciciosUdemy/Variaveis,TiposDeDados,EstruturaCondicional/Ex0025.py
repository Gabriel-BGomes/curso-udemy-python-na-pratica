#Escreva um programa que receba dois números de ponto flutuante e mostre na tela o maior número digitado. Considere a possibilidade de o usuário digitar dois números iguais.

n1=float(input('Valor 1 : '))
n2=float(input('Valor 2 : '))

if n1>n2:
    print(f'{n1}>{n2}')
elif n1==n2:
    print(f'{n1}={n2}')
else:
    print(f'{n1}<{n2}')