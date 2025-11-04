#Escreva um programa que peça um número inteiro do usuário e mostre na tela o fatorial deste número.

n = int(input("Digite um numéro para fazer o fatorial do mesmo: "))

fatorial = 1
for i in range (1,n+1):
    fatorial = fatorial * i
for f in range (n,-1,-1):
    print(f'{f}!')
print(f'O fatorial de {n}! é {fatorial}')
