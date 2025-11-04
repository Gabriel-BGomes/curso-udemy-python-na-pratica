#Escreva um programa que solicite duas notas do usuário e apresente a média na tela da seguinte forma:

#"A média das notas [nota1] e [nota2] é [média]"

n1 = float(input("Digite a sua primeira nota:"))
n2 = float(input("Digite a sua segunda nota:"))

media = (n1+n2)/2

print(f'A média das notas {n1} e {n2} é {media}')