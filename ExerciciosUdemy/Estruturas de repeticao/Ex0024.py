#Escreva um programa para checar se um determinando número é primo ou não.

#Lembrete: Um número primo pode ser dividido por apenas dois números, quais sejam: ele mesmo e o número um.

#2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,83,89 e 97 (Números primos entre 1 e 100)

n = int(input("Digite um número primo: "))

if n>1:
    for i in range(2, n):
        if n % i == 0:
            print(f'O número {n} não é primo')
            break
    else:
        print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo')