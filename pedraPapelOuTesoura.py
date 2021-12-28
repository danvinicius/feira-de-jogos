import random
from os import system
from time import sleep


def pedraPapelOuTesoura(jogador):
    jogarNovamente = True
    while jogarNovamente == True:
        system("cls || clear")
        print("Pedra, papel ou tesoura")
        jogador.diminuiCreditos(2)
        vitoriasMaquina = 0
        vitoriasJogador = 0
        rodada = 1
        opcoes = ["Pedra", "Papel", "Tesoura"]

        while rodada < 4 and vitoriasJogador < 2 and vitoriasMaquina < 2:
            sleep(1)
            system("cls || clear")
            print("=-=-=-=-=-=-=-=-=-=-=-")
            print(f"Jogador {vitoriasJogador} x {vitoriasMaquina} Máquina")
            print(f"Rodada: {rodada}/3")
            print("=-=-=-=-=-=-=-=-=-=-=-")
            print("Faça sua jogada: ")
            while True:
                escolhaJogador = input("[1] Pedra\n" + "[2] Papel\n" + "[3] Tesoura\n")
                if not escolhaJogador.isnumeric():
                    print("Digite apenas números")
                if not (
                    escolhaJogador == "1"
                    or escolhaJogador == "2"
                    or escolhaJogador == "3"
                ):
                    print("Escolha uma jogada entre 1 e 3")
                else:
                    escolhaJogador = int(escolhaJogador)
                    break
            escolhaJogador = opcoes[escolhaJogador - 1]
            escolhaMaquina = random.choice(opcoes)
            sleep(1)
            print(f"Jogador: {escolhaJogador}")
            sleep(1)
            print(f"Máquina: {escolhaMaquina}")
            sleep(1)

            # Casos de vitória da máquina
            if (
                escolhaMaquina == "Pedra"
                and escolhaJogador == "Tesoura"
                or escolhaMaquina == "Tesoura"
                and escolhaJogador == "Papel"
                or escolhaMaquina == "Papel"
                and escolhaJogador == "Pedra"
            ):
                vitoriasMaquina += 1
                print("Máquina vence!")
                rodada += 1
            # Casos de vitória do jogador
            elif (
                escolhaJogador == "Pedra"
                and escolhaMaquina == "Tesoura"
                or escolhaJogador == "Tesoura"
                and escolhaMaquina == "Papel"
                or escolhaJogador == "Papel"
                and escolhaMaquina == "Pedra"
            ):
                vitoriasJogador += 1
                print("Jogador vence!")
                rodada += 1
            # Empate
            else:
                print("Empate!")

        print("=-=-=-=-=-=-=-=-=-=-=-")
        print(f"Jogador {vitoriasJogador} x {vitoriasMaquina} Máquina")
        if vitoriasJogador > vitoriasMaquina:
            jogador.pontos += 200
            print("Jogador venceu a partida!")
        elif vitoriasMaquina > vitoriasJogador:
            print("Máquina venceu a partida!")
        else:
            print("A partida empatou!")
        print("=-=-=-=-=-=-=-=-=-=-=-")

        while True:
            resposta = input("Deseja jogar novamente? (S/N)\n")
            if resposta in "nN":
                jogarNovamente = False
                break
            elif resposta in "sS":
                break
            elif resposta not in "sSnN":
                print("Responda somente com 'S' ou 'N'")
