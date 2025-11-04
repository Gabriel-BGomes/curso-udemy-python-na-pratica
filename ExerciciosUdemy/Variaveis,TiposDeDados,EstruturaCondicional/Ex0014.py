#Escreva um programa que peça o nome e a idade do usuário. Caso a idade do usuário seja maior ou igual a 18 anos apresente a seguinte mensagem: "Seja bem-vindo ao nosso site [nome]!"; caso contrário, apresente a seguinte mensagem: "Você não pode acessar nosso site [nome].".

nome=input('Digite seu nome: ')
idade=int(input('Digite sua idade: '))
if idade>=18:
    print(f'Seja bem-vindo ao nosso site {nome.strip().title()}.')
else:
    print(f'Você não pode acessar nosso site {nome.strip().title()}.')