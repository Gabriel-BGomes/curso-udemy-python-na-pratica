#Elabore um programa para verificar se um ano é bisexto ou não. A condição para ser um ano bisexto é: o ano deve ser divisível por 400; ou se for divisível por 4 e não for divisível por 100.

ano = int(input("Digite um ano: ")) #Exemplo de entrada (2020)

if ano%400 == 0 or (ano%4==0 and not ano%100 == 0):
    print(f'{ano} é um ano bisexto')
else:
    print(f'Não é bisexto')