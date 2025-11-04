# Implemente uma calculadora simples com as operações aritméticas básicas. O usuário deverá especificar a operação desejada (+,-,*,/) e seguidamente inserir dois valores. Caso, o usuário escolha divisão e insera o valordo denominar 0 mostra uma mensagem personalizada. Para os demais casos, mostre na tela o resultado da operação desejada.

print("Bem-Vindo à calculadora! \n(+,-,x,/)")
print("\ndigite 1 para +")
print("digite 2 para -")
print("digite 3 para x")
print("digite 4 para /")

opcao = int(input("Escolha a operação que deseja: "))

n1 = int(input("Digite o 1º número:"))
n2 = int(input("Digite o 2º número:"))

if opcao == 1:
    print(f'{n1} + {n2} = {n1+n2}')
elif opcao == 2:
    print(f'{n1} - {n2} = {n1-n2}')
elif opcao == 3:
    print(f'{n1} x {n2} = {n1*n2}')
else:
    print(f'{n1} / {n2} = {n1/n2}')