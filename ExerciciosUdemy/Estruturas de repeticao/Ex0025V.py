#Elabore um programa para imprimir todos os números primos existentes em um intervalo delimitado pelo usuário

numeros_primos_min = int(input("Digite um número minimo de números primos que você deseja: "))
numeros_primos_max = int(input("Digite um número máximo de números primos que você deseja: "))
    
for numero in range (numeros_primos_min, numeros_primos_max+1):
    if numero>1:
        for j in range (2, numero):
            if numero % j == 0:
                break
            else:
                print(f'{numero}')