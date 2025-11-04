# Escreva um programa que peça números reais (float) do usuário indefinidamente. Caso os números digitados não sejam situados entre 0 e 10 o programa deverá ser finalizado, mostrando a soma e a quantidade de números digitados.

n = 0
soma = 0
cont = 0
while n>=0 and n<=10:
    n = float(input("Digite um número entre 0-10, caso queira finalizar o programa, digite um número fora dos parâmetros.")) 
    cont += 1
    if n>=0 and n<=10:
        soma += n
    else:
        print(f'A soma de todos os números digitados foram: {soma}\n A quantidade de números digitados foram: {cont}')
    
