#Escreva um programa que peça números inteiros positivos indefinidamente e armazene-os em uma lista. O programa deverá ser encerrado caso o número digitado seja negativo ou nulo. Ao final mostre na tela a quantidade de números pares e ímpares.

numeros_inteiros = []
contp = 0
conti = 0
n=0

while n>=0:
    n = int(input("Digite um número para ser armazenado na lista:"))
    if n>0:
        numeros_inteiros.append(n)
    else:
        print(f'O programa foi encerrado.')
        break
            
    if n%2==0:
        contp+= 1
    else:
        conti+=1
    
print(f'ímpar: {conti}\n par: {contp}')
    
    
    


