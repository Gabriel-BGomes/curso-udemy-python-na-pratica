#Faça um programa que calcule a raiz quadrada de um número. O usuário deve inserir um número e o programa deve mostrar na tela o resultado da raiz quadrada do número inserido.

import math

n = int(input("Digite um número:"))

if n<0:
    print("Raiz negativa não é real.")
else:
    raiz = math.sqrt(n)
    print(f"A raiz quadrada de {n} é {raiz:.2f}")

