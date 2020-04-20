class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1


    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0

    def calcular_velocidade(self):
        print(self.velocidade)