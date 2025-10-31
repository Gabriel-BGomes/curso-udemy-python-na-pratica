#Escreva um programa que peça um número inteiro do usuário e calcule e imprima a tabuada deste número.

n = int(input("Digite um número para ser impresso a sua tabuada: \n"))

for i in range(11):
    print(f'{n} x {i} = {n*i}')
    