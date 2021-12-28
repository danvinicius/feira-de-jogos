from time import sleep
from os import system
from jogoDaForca import jogoDaForca
from jogoDaVelha import jogoDaVelha
from pedraPapelOuTesoura import pedraPapelOuTesoura
from adivinheONumero import adivinheONumero
from Jogador import Jogador

continua = True

system("cls || clear")
print("Bem-vindo à feira de jogos")
sleep(1)
nome = input("Me diga qual é seu nome: ").capitalize()
jogador = Jogador(nome=nome, creditos=20, pontos=0)
system("cls || clear")
print(f"Olá, {jogador.nome}! Que bom recebê-la(o) aqui.")
sleep(2)
print("Você começa com 20 créditos e perde 2 a cada partida jogada")
sleep(2)
print("O objetivo é conseguir 1000 pontos antes dos seus créditos acabarem")
sleep(2)
print("Será que você consegue?")
sleep(2)


def mostrarJogos():
    system("cls || clear")
    print(f"Escolha seu jogo: ")
    while True:
        jogoEscolhido = input(
            "[1] Adivinhe o número\n"
            + "[2] Pedra, papel e tesoura\n"
            + "[3] Jogo da forca\n"
            + "[4] Jogo da velha\n"
        )
        if not jogoEscolhido.isnumeric():
            system("cls || clear")
            print("Digite apenas números")
        if not (
            jogoEscolhido == "1"
            or jogoEscolhido == "2"
            or jogoEscolhido == "3"
            or jogoEscolhido == "4"
        ):
            print("Escolha um jogo entre 1 e 4")
        else:
            if jogoEscolhido == "1":
                adivinheONumero(jogador)
            elif jogoEscolhido == "2":
                pedraPapelOuTesoura(jogador)
            elif jogoEscolhido == "3":
                jogoDaForca(jogador)
            elif jogoEscolhido == "4":
                jogoDaVelha(jogador)
            break


mostrarJogos()


def mostrarMenuPrincipal():
    global continua
    while True:
        acao = input(
            "[1] Mostrar jogos\n"
            + "[2] Mostrar estatísticas do jogador\n"
            + "[3] Sair\n"
        )
        if not acao.isnumeric():
            system("cls || clear")
            print("Digite apenas números")
        if not (acao == "1" or acao == "2" or acao == "3"):
            print("Escolha uma ação entre 1 e 3: ")
        else:
            if acao == "1":
                mostrarJogos()
            if acao == "2":
                mostrarEstatisticas()
            if acao == "3":
                print("Bye bye \(≧◡≦)/")
                continua = False
            break


def mostrarEstatisticas():
    system("cls || clear")
    print(
        "=-=-=-=-=-=-=-=-=-=-=-=-\n"
        + f"Nome: {jogador.nome}\n"
        + "=-=-=-=-=-=-=-=-=-=-=-=-\n"
        + f"Créditos: {jogador.creditos}\n"
        + "=-=-=-=-=-=-=-=-=-=-=-=-\n"
        + f"Pontuação: {jogador.pontos} pontos\n"
        + "=-=-=-=-=-=-=-=-=-=-=-=-"
    )


def reiniciar():
    system("cls || clear")
    system("py main.py || python3 main.py")


while jogador.creditos > 0 and continua:
    if jogador.pontos >= 1000:
        print("\(≧◡≦)/")
        print("Parabéns, você ganhou a feira de jogos!")
        print(
            "=-=-=-=-=-=-=-=-=-=-=-=-\n"
            + f"Nome: {jogador.nome}\n"
            + "=-=-=-=-=-=-=-=-=-=-=-=-\n"
            + f"Créditos: {jogador.creditos}\n"
            + "=-=-=-=-=-=-=-=-=-=-=-=-\n"
            + f"Pontuação: {jogador.pontos} pontos\n"
            + "=-=-=-=-=-=-=-=-=-=-=-=-"
        )
        while True:
            acao = input("[1] Reiniciar\n" + "[2] Sair\n")
            if not acao.isnumeric():
                system("cls || clear")
                print("Digite apenas números")
            if not (acao == "1" or acao == "2"):
                print("Escolha uma ação entre 1 e 2: ")
            else:
                if acao == "1":
                    reiniciar()
                if acao == "2":
                    print("Bye bye \(≧◡≦)/")
                    continua = False
                break
    mostrarMenuPrincipal()
