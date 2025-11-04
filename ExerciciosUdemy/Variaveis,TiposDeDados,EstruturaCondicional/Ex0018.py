#Faça um programa que peça a base e a altura de um retângulo e calcule e mostre na tela a área e o perímetro.

base=float(input('Digite a base do retângulo: '))
altura=float(input('Digite a altura do retângulo: '))
 
area=base*altura
perimetro=2*base+2*altura
 
print(f'O retângulo digitado tem base {base} e altura {altura}.')
print(f'A área deste retângulo é: {area}')
print(f'O perímetro deste retângulo é: {perimetro}')