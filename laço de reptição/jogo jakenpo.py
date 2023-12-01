import random

opcoes = ["pedra", "papel", "tesoura"]
jogando = True

while jogando:
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    computador = random.choice(opcoes)

    print(f"Computador escolheu: {computador}")

    if jogador in opcoes:
        if jogador == computador:
            print("Empate!")
        elif jogador == "pedra":
            if computador == "papel":
                print("Computador venceu!")
            else:
                print("Jogador venceu!")
        elif jogador == "papel":
            if computador == "tesoura":
                print("Computador venceu!")
            else:
                print("Jogador venceu!")
        elif jogador == "tesoura":
            if computador == "pedra":
                print("Computador venceu!")
            else:
                print("Jogador venceu!")
    else:
        print("Escolha inválida. Escolha entre pedra, papel ou tesoura.")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        jogando = False