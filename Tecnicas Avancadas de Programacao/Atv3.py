#exercicio

votos = [0] * 23

print("Enquete: Quem foi o melhor jogador em campo? ")
print("Digite um numero entre 1 e 23 para votar ou 0 para sair: ")

while True:
  try:
    num = int(input("Numero do melhor jogador (1-23 ou 0 para encerrar):"))
    if num == 0:
      print(votos)
      break
    elif 1 <= num <= 23: #ou posso escrever: elif num >=1 and num <=23:
      votos[num-1] += 1 # x=x+1 ou x+=1
    else:
      print("Numero invalido! Digite um número entre 1 e 23!")
  except ValueError:
    print("Valor invalido")

    #impressão dos resultados

    total_votos = sum(votos)
    print("\n===== Resultado da enquete: =====")
    print(f"Total de votos computados: {total_votos}\n")
    if total_votos == 0:
      print("Nenhum jogador recebeu votos!")
    else:
      print("Jogador | Votos | Percentual")
      print("----------+--------+-----------------")

    melhor_jogador = 0

    for i in range(23):
      if votos[i] > 0:
        percentual = (votos[i] / total_votos) * 100
        print(f"{i+1} | {votos[i]} | {percentual:.2f}%")

        if votos[i] > votos[melhor_jogador]:
          melhor_jogador = i