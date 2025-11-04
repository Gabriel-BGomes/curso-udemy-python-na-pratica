#Elabore um programa que embaralhe a lista a seguir e mostre n atela cada elemento.

#lista = ['A','B','C','D','E','F','G'...]

#O output do programa pode seguir o padrão abaixo:

'''
A
C
B
K
J
F
M
D
H
G
L
I
E
''' 
import random
lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M']

random.shuffle(lista)
print(lista)