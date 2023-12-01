tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador_atual = "X"
jogando = True

while jogando:
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

    linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1 ou 2): "))
    coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2): "))

    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador_atual

        # Verificar vitória
        vitoria = False
        for i in range(3):
            if all([tabuleiro[i][j] == jogador_atual for j in range(3)]) or all([tabuleiro[j][i] == jogador_atual for j in range(3)]):
                vitoria = True
                break
        if all([tabuleiro[i][i] == jogador_atual for i in range(3)]) or all([tabuleiro[i][2 - i] == jogador_atual for i in range(3)]):
            vitoria = True

        if vitoria:
            for linha in tabuleiro:
                print(" | ".join(linha))
                print("-" * 9)
            print(f"Jogador {jogador_atual} venceu!")
            jogando = False
        else:
            jogador_atual = "X" if jogador_atual == "O" else "O"
    else:
        print("Essa posição já está ocupada. Escolha outra.")

    if all([tabuleiro[i][j] != " " for i in range(3) for j in range(3)]):
        for linha in tabuleiro:
            print(" | ".join(linha))
            print("-" * 9)
        print("Empate!")
        jogando = False