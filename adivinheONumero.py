import random
from os import system
from time import sleep


def adivinheONumero(jogador):
    jogarNovamente = True
    while jogarNovamente == True:
        system("cls || clear")
        print("Adivinhe o número")
        sleep(1)
        jogador.diminuiCreditos(2)
        tentativas = 7
        numeroMagico = random.randint(0, 100)
        print("Pensei em um número de 0 a 100, você consegue adivinhar ele?")
        sleep(1)
        print("Você tem 7 tentativas")
        sleep(1)

        while tentativas > 0:
            while True:
                palpite = input("Em que número eu pensei? \n")
                if not palpite.isnumeric():
                    print("Digite apenas números")
                else:
                    palpite = int(palpite)
                    break
            if palpite < numeroMagico:
                print(f"O número que eu pensei é MAIOR do que {palpite}")
                tentativas -= 1
            elif palpite > numeroMagico:
                print(f"O número que eu pensei é MENOR do que {palpite}")
                tentativas -= 1
            if palpite == numeroMagico:
                print("Parabéns, você acertou!")
                jogador.aumentaPontos(200)
                break
        if tentativas == 0:
            print("Suas chances acabaram :(")
            print(f"O número era {numeroMagico}")

        while True:
            resposta = input("Deseja jogar novamente? (S/N)\n")
            if resposta in "nN":
                jogarNovamente = False
                break
            elif resposta in "sS":
                break
            elif resposta not in "sSnN":
                print("Responda somente com 'S' ou 'N'")
