#Escreva um programa que receba três números do usuário e mostre na tela o maior número digitado.

n1 = int(input(f"Digite o 1º número: "))
n2 = int(input(f"Digite o 2º número: "))
n3 = int(input(f"Digite o 3º número: "))

if n1!=n2 and n1!=n3 and n2!=n3:
    if n1>n2 and n1>n3:
        print(n1)
    elif n2>n1 and n2>n3:
        print(n2)
    else:
        print(n3)
else:
    print(f'Este programa não aceita números iguais.')