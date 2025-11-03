#Ultilizando estruturas de repetição escreva um programa que mostre os resultados da tauada de multiplicação dos números entre 1 e 10, como segue.

'''
1 x 1 = 1 ...

2 x 2 = 4 ...

'''

for i in range (11):
    print("\n")
    for n in range (11):
        print(f'{i} x {n} = {i*n}')