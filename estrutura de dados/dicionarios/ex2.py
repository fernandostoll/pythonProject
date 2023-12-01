import random
# Função para lançar um dado de 6 lados
def lancar_dado():
    return random.randint(1, 6)

# Dicionário para armazenar os resultados dos jogadores
resultados = {}

# Simular o lançamento de dados para 4 jogadores
for jogador in range(1, 5):
    resultado = lancar_dado()
    resultados[f"Jogador {jogador}"] = resultado

# Exibir os resultados antes da ordenação
print("Resultados dos Jogadores (antes da ordenação):")
for jogador, resultado in resultados.items():
    print(f"{jogador}: {resultado}")

# Ordenar o dicionário com base nos resultados (maior resultado primeiro)
resultados_ordenados = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))

# Exibir os resultados ordenados
print("\nResultados dos Jogadores (após a ordenação):")
for jogador, resultado in resultados_ordenados.items():
    print(f"{jogador}: {resultado}")

# Identificar o vencedor (jogador com o maior resultado)
vencedor = next(iter(resultados_ordenados))
print(f"\nO vencedor é {vencedor} com o resultado {resultados_ordenados[vencedor]}!")