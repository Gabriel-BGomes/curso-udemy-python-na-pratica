#Escreva um programa que peça ao usuário números entre 0-10. Se o usuário inserir um número fora desse intervalo o programa deverá finalizar com uma mensagem personalizada.
n=0

while n>=0 and n<=10:
    n = int(input("Digite um número entre 0-10. Caso deseje finalizar o programa digite um número fora desse parametro. "))    
print("Finalizado.")