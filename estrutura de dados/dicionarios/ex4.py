#nome do jogador
nome_jogador = input('Digite o nome do jogador: ')

#quantidade de partidas
quantidade_partidas = int(input(f'Quantas partidas {nome_jogador} jogou? '))

#aproveitamento do jogador
aproveitamento = {'nome': nome_jogador, 'partidas jogadas': quantidade_partidas}

#cada gols por partidadas
gols_por_partida = []

#quantidade de gol partida
for partida in range(quantidade_partidas):
    gols = int(input(f'quantos gols {nome_jogador} fez na partida {partida + 1}? '))
    gols_por_partida.append(gols)

#gol durante o campeonato
total_gols = sum(gols_por_partida)

#gols por partida e total de gol
aproveitamento["Gols por Partida"] = gols_por_partida
aproveitamento["Total de gols"] = total_gols

#aproveitamento do jogador
print('\nAproveitamento do jogador: ')
for chave, valor in aproveitamento.items():
    print(f'{chave}: {valor}')