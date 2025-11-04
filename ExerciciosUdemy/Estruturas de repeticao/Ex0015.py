#Elabore um programa que calcule e mostre na tela os números ímpares entre 1 e 200. Os números devem ser mostrados na tela de acordo com o formato a seguir:

#1 3 5 7 9 11 13 15 17 19 21 23 25 27 ...

for i in range (200):
    if i%2==1: #Eu poderia ter colocado também assim: (if i%2!=0:)
        print(i)