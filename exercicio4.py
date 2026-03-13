notas = [float(input(f"digite a {i+1} nota: ")) for i in range(4)]

media = sum(notas) / len(notas)

print(f"a media final do aluno é {media:.2f}")
