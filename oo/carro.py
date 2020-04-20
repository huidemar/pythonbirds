'''
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1 - Motor
2 - Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

1 - Atributo de dado velocidade
2 - Método acelerar, que deverá incremetar a velocidade de uma unidade
3 - Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:

1 - Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
2 - Método girar_a_direita
3 - Método girar_a_esquerda

'''
from direcao import Direcao
from motor import Motor

class Carro:
    def __init__(self, motor=Motor(), direcao=Direcao()):
        self.motor = motor
        self.direcao = direcao


mot = Motor()
dir = Direcao()

car = Carro(motor=mot, direcao=dir)
car.direcao.girar_a_direita()
car.direcao.calcular_direcao()
