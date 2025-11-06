#Considere um número inteiro positivo n especificado pelo usuário .Elabore um programa que calcule e mostre na tela:

#*A soma dos n primeiros números inteiros não-nulos (1+2+3+...+n);

#*A soma dos n primeiros números pares;

#* A soma dos n primeiros números ímpares;

n = int(input("Digite um número: "))
soma = 0
somap = 0
somai = 0
if n>0:
    for i in range (1,n+1):
        soma += i
        if i%2 == 0:
            somap += i
        elif i%2 == 1:
            somai += i
        if i==n:
            print(f'A soma dos n primeiros números inteiros é: {soma}')
            print(f' soma dos n primeiros números pares é: {somap}')
            print(f' soma dos n primeiros números ímpares é: {somai}')
else:
    print('O valor digitado não é válido.')