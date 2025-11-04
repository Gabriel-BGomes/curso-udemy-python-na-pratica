#Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar. A mensagem na tela deverá seguir o seguinte formato:

#"O número [número] é [par/ímpar]"

n = int(input("Digite um número: "))

if n%2==0:
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é ímpar.')