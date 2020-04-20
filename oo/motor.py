class Motor:
'''
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1 - Atributo de dado velocidade
2 - Método acelerar, que deverá incremetar a velocidade de uma unidade
3 - Método frear que deverá decrementar a velocidade em duas unidades
'''
    def __init__(self, velocidade=0):
        self.velocidade = velocidade


    def acelerar(self):
        self.velocidade += 1


    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0

