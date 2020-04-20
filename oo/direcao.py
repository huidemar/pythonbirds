class Direcao:
    def __init__(self, valor='Norte'):
        self.rota = ['Norte', 'Leste', 'Sul', 'Oeste']
        self.valor = valor
        self.direcao = self.rota.index(self.valor)

    def girar_a_direita(self):
        if self.direcao == len(self.rota)-1:
            self.direcao = 0
        else:
            self.direcao += 1
        self.valor = self.rota[self.direcao]

    def girar_a_esquerda(self):
        if self.direcao == 0:
            self.direcao = len(self.rota)-1
        else:
            self.direcao -= 1
        self.valor = self.rota[self.direcao]

    def calcular_direcao(self):
        return self.valor