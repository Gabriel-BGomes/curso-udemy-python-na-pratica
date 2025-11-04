#Escreva um programa que peça números inteiros não nulos ao usuário e mostra na tela o quadrado de cada número digitado.

lista = []
for i in range (1,6):
    num=int(input(f'Digite o {i}º número: '))
    if num>0:
        lista.append(num)
    if i == 5:
        for n in lista:
            print(f'O quadrado de {n} é: {n**2}')