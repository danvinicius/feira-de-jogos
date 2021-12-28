class Jogador:
    def __init__(self, nome, creditos, pontos):
        self.nome = nome
        self.creditos = creditos
        self.pontos = pontos

    def diminuiCreditos(self, creditos):
        self.creditos -= creditos

    def aumentaPontos(self, pontos):
        self.pontos += pontos

    def diminuiPontos(self, pontos):
        self.pontos -= pontos
