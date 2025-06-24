# (a) Entrada de dados
N = int(input("Digite o número de candidatos: "))

nomes = []
medias = []

for i in range(N):
    print(f"\nCandidato {i+1}:")
    nome = input("Nome: ")
    nota1 = float(input("Nota de Matemática: "))
    nota2 = float(input("Nota de Português: "))
    nota3 = float(input("Nota de Física: "))

    media = (nota1 + nota2 + nota3) / 3
    nomes.append(nome)
    medias.append(media)

# (b) Ordenar por média
# Juntamos nome e média em uma lista de tuplas, depois ordenamos por média
candidatos = list(zip(nomes, medias))
candidatos_ordenados = sorted(candidatos, key=lambda x: x[1])

# Exibir relatório
print("\nRELATÓRIO DE CLASSIFICAÇÃO:")
print("NOME     MÉDIA")
for nome, media in candidatos_ordenados:
    print(f"{nome:<8} {media:.2f}")
