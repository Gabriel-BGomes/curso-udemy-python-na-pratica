notas = {
    "gabriel": 10,
    "joao": 9,
    "maria": 8,
    "pedro": 7,
    "ana": 6
}

# Calcula a média da turma
media = sum(notas.values()) / len(notas)

# Exibe o resultado
print("Notas dos alunos:")
for aluno, nota in notas.items():
    print(f"{aluno}: {nota}")

print(f"\nMédia da turma: {media:.2f}")