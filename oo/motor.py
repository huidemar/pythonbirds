'''
    >>> #Testando motor
    >>> motor = Motor()
    >>> motor.acelerar()
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.frear()
    >>> motor.frear()
'''
class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1


    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0

    def calcular_velocidade(self):
        print(self.velocidade)