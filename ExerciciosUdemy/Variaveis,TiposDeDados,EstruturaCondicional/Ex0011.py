#Escreva um programa que peça dois números e apresente a divisão e multiplicação entre eles. A tela de apresentação deverá seguir o seguinte formato:

#"[número1]x[número2]=[multiplicação]"

#"[número1]/[número2]=[divisão]

n1 = int(input("Digite o 1º número: \n"))
n2 = int(input("Digite o 2º número: \n"))

#Multiplicação:
print(f'{n1} x {n2} = {n1*n2}')

#Divisão:
print(f'{n1} / {n2} = {n1/n2}')