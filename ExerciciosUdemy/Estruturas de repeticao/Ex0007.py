#Ultilizando estruturas de repetição escreva um programa que mstre os resultados da tabuada (multiplicação) de um número inserido pelo usuário.

n = int(input("Digite a tabuada do número que você quer: "))

for i in range (11):
    print(f'{n} x {i} = {n*i}')