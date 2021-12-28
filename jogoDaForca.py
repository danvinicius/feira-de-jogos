from random import choice
from os import system


def jogoDaForca(jogador):
    jogarNovamente = True
    while jogarNovamente == True:
        system("cls || clear")
        print("Jogo da forca")
        jogador.diminuiCreditos(2)

        listaPalavras = [
            [
                "Animal",
                [
                    "cachorro",
                    "elefante",
                    "crocodilo",
                    "hipopotamo",
                    "canguru",
                    "gafanhoto",
                    "rinoceronte",
                ],
            ],
            [
                "Objeto",
                [
                    "guitarra",
                    "microfone",
                    "ventilador",
                    "roteador",
                    "escada",
                    "amortecedor",
                    "borracha",
                    "computador",
                ],
            ],
            [
                "Fruta",
                [
                    "abacaxi",
                    "pessego",
                    "goiaba",
                    "graviola",
                    "kiwi",
                    "tangerina",
                    "ameixa",
                    "acerola",
                ],
            ],
            [
                "País",
                [
                    "mexico",
                    "noruega",
                    "dinamarca",
                    "argentina",
                    "tailandia",
                    "australia",
                    "venezuela",
                    "nigeria",
                ],
            ],
        ]

        # Definindo a palavra e sua dica
        grupoDePalavras = choice(listaPalavras)
        dica = grupoDePalavras[0]
        palavraSecreta = choice(grupoDePalavras[1])

        letrasAcertadas = []
        ganhou = False
        erros = 0
        letrasErradas = ""
        while erros < 6:
            system("cls || clear")
            palavraCifrada = ""
            print("Dica: " + dica)
            print(letrasErradas.upper())
            if erros == 0:
                print(
                    """
        -------x
        ||     |
        ||     | 
        ||     |
        || 
        ||  
        ||
        ||
        ||
        ||
        ||"""
                )
            elif erros == 1:
                print(
                    """
        -------x
        ||     |
        ||     | 
        ||   __|__
        ||  / o o \\
        ||  \__=__/
        ||
        ||
        ||
        ||
        ||"""
                )
            elif erros == 2:
                print(
                    """
        -------x
        ||     |
        ||     | 
        ||   __|__
        ||  / o o \\
        ||  \__=__/
        ||     |
        ||     | 
        ||
        ||
        ||"""
                )
            elif erros == 3:
                print(
                    """
        -------x
        ||     |
        ||     | 
        ||   __|__
        ||  / o o \\
        ||  \__=__/
        ||    /|
        ||   / |
        ||
        ||
        ||"""
                )
            elif erros == 4:
                print(
                    """
        -------x
        ||     |
        ||     | 
        ||   __|__
        ||  / o o \\
        ||  \__=__/
        ||    /|\\
        ||   / | \\
        ||
        ||
        ||"""
                )
            elif erros == 5:
                print(
                    """
        -------x
        ||     |
        ||     | 
        ||   __|__
        ||  / o o \\
        ||  \__=__/
        ||    /|\\
        ||   / | \\
        ||    /
        ||   /
        ||"""
                )

            for letra in palavraSecreta:
                palavraCifrada += (letra) if letra in letrasAcertadas else "_"

            # Verifica se o usuário já acertou
            if palavraCifrada == palavraSecreta:
                ganhou = True
                break

            # Usuário digita a letra
            while True:
                print("Palavra: " + palavraCifrada.replace("", " "))
                tentativa = input("Digite uma letra: \n").lower()
                if tentativa.isalpha() == False or len(tentativa) != 1:
                    print(
                        "Digite apenas uma letra e não digite números ou caracteres especiais\n"
                    )
                elif (tentativa in letrasAcertadas) or (tentativa in letrasErradas):
                    print("Você já digitou essa letra\n")
                else:
                    if tentativa in palavraSecreta:
                        letrasAcertadas.append(tentativa)
                    else:
                        letrasErradas += tentativa + " "
                        erros += 1
                    break

        if ganhou == True:
            jogador.pontos += 200
            print("Parabéns, Você acertou!!")
        else:
            system("cls || clear")
            print(letrasErradas)
            print(
                """
        -------x
        ||     |
        ||     | 
        ||   __|__
        ||  / x x \\
        ||  \__=__/
        ||    /|\\
        ||   / | \\
        ||    / \\
        ||   /   \\
        ||"""
            )
            print("Você perdeu :(")
            print("A palavra era " + palavraSecreta.upper())

        while True:
            resposta = input("Deseja jogar novamente? (S/N)\n")
            if resposta in "nN":
                jogarNovamente = False
                break
            elif resposta in "sS":
                break
            elif resposta not in "sSnN":
                print("Responda somente com 'S' ou 'N'")
