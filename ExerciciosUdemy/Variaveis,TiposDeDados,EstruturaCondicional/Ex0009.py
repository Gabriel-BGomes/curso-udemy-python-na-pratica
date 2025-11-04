#Escreva um programa que calcule a área de uma circunferência. O usuário deve digitar o valor do raio e ao final o programa deverá mostrar na tela a área da circunferência.

#Use a fórmula: área=pi*r² , em que pi é uma constante e r o raio da circunferência.

#Dica: você pode usar a biblioteca math para pegar a constante pi.

from math import pi

raio = float(input("Digite o raio da circuferência: "))
print(f'Área da circunferência: {pi*raio**2:.2f}')

