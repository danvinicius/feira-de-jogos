import random
from os import system


def jogoDaVelha(jogador):
    jogarNovamente = True
    while jogarNovamente == True:
        system("cls || clear")
        jogador.diminuiCreditos(2)
        jogadorVenceu = False
        maquinaVenceu = False
        rodada = 0
        tabuleiro = list(range(0, 9))
        print("Tabuleiro: ")
        print(
            f"{'1':^5}|{'2':^5}|{'3':^5}\n-----+-----+-----\n{'4':^5}|{'5':^5}|{'6':^5}\n-----+-----+-----\n{'7':^5}|{'8':^5}|{'9':^5}\n"
        )
        for i in range(0, 9):
            tabuleiro[i] = " "

        while jogadorVenceu == False or maquinaVenceu == False or rodada < 4:

            # Jogador deve escolher entre 1 e 9
            print("Escolha uma posição: ")
            while True:
                escolhaJogador = input(
                    f"{tabuleiro[0]:^5}|{tabuleiro[1]:^5}|{tabuleiro[2]:^5}\n-----+-----+-----\n{tabuleiro[3]:^5}|{tabuleiro[4]:^5}|{tabuleiro[5]:^5}\n-----+-----+-----\n{tabuleiro[6]:^5}|{tabuleiro[7]:^5}|{tabuleiro[8]:^5}\n"
                )
                if not escolhaJogador.isnumeric():
                    print("Digite apenas números")
                elif not (0 < int(escolhaJogador) <= 9):
                    print("Escolha uma jogada entre 1 e 9")
                else:
                    escolhaJogador = int(escolhaJogador)
                    break

            # Jogador joga
            if tabuleiro[escolhaJogador - 1] != " ":
                while tabuleiro[escolhaJogador - 1] != " ":
                    print("Essa posição já foi escolhida")
                    escolhaJogador = int(input("Escolha outra posição: "))
            tabuleiro[escolhaJogador - 1] = "X"
            # Verifica vitória do jogador

            ##vitória na vertical
            if (
                (tabuleiro[0] == "X" and tabuleiro[3] == "X" and tabuleiro[6] == "X")
                or (tabuleiro[1] == "X" and tabuleiro[4] == "X" and tabuleiro[7] == "X")
                or (tabuleiro[2] == "X" and tabuleiro[5] == "X" and tabuleiro[8] == "X")
            ):
                jogadorVenceu = True
                break

            ##vitória na horizontal
            elif (
                tabuleiro[0] == "X"
                and tabuleiro[1] == "X"
                and tabuleiro[2] == "X"
                or tabuleiro[3] == "X"
                and tabuleiro[4] == "X"
                and tabuleiro[5] == "X"
                or tabuleiro[6] == "X"
                and tabuleiro[7] == "X"
                and tabuleiro[8] == "X"
            ):
                jogadorVenceu = True
                break

            ##vitória na diagonal
            elif (
                tabuleiro[0] == "X"
                and tabuleiro[4] == "X"
                and tabuleiro[8] == "X"
                or tabuleiro[2] == "X"
                and tabuleiro[4] == "X"
                and tabuleiro[6] == "X"
            ):
                jogadorVenceu = True
                break

            if rodada == 4:
                break

            # Máquina joga
            escolhaMaquina = random.randint(0, 9)
            while tabuleiro[escolhaMaquina - 1] != " ":
                escolhaMaquina = random.randint(0, 9)
            tabuleiro[escolhaMaquina - 1] = "O"

            # Verifica vitória da máquina
            ##vitória na vertical
            if (
                tabuleiro[0] == "O"
                and tabuleiro[3] == "O"
                and tabuleiro[6] == "O"
                or tabuleiro[1] == "O"
                and tabuleiro[4] == "O"
                and tabuleiro[7] == "O"
                or tabuleiro[2] == "O"
                and tabuleiro[5] == "O"
                and tabuleiro[8] == "O"
            ):
                maquinaVenceu = True
                break

            ##vitória na horizontal
            elif (
                tabuleiro[0] == "O"
                and tabuleiro[1] == "O"
                and tabuleiro[2] == "O"
                or tabuleiro[3] == "O"
                and tabuleiro[4] == "O"
                and tabuleiro[5] == "O"
                or tabuleiro[6] == "O"
                and tabuleiro[7] == "O"
                and tabuleiro[8] == "O"
            ):
                maquinaVenceu = True
                break

            ##vitória na diagonal
            elif (
                tabuleiro[0] == "O"
                and tabuleiro[4] == "O"
                and tabuleiro[8] == "O"
                or tabuleiro[2] == "O"
                and tabuleiro[4] == "O"
                and tabuleiro[6] == "O"
            ):
                maquinaVenceu = True
                break

            rodada += 1
        print(
            f"{tabuleiro[0]:^5}|{tabuleiro[1]:^5}|{tabuleiro[2]:^5}\n-----+-----+-----\n{tabuleiro[3]:^5}|{tabuleiro[4]:^5}|{tabuleiro[5]:^5}\n-----+-----+-----\n{tabuleiro[6]:^5}|{tabuleiro[7]:^5}|{tabuleiro[8]:^5}\n"
        )
        if maquinaVenceu and jogadorVenceu == False:
            print("Máquina venceu")
        elif jogadorVenceu and maquinaVenceu == False:
            print("Jogador venceu")
            jogador.aumentaPontos(200)
        elif jogadorVenceu == False and maquinaVenceu == False:
            print("Deu velha")

        while True:
            resposta = input("Deseja jogar novamente? (S/N)\n")
            if resposta in "nN":
                jogarNovamente = False
                break
            elif resposta in "sS":
                break
            elif resposta not in "sSnN":
                print("Responda somente com 'S' ou 'N'")
