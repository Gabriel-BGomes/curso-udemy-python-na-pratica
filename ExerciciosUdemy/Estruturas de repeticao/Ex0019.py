#Peça 5 números do usuário e mostre na tela a média dos números digitados

soma = 0

for i in range (1,6):
    n = int(input(f'Digite o {i}º número: '))
    soma+=n
print(f'Média: {soma/5}')