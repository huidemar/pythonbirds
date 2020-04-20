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

    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.acelerar()
    >>> motor.acelerar()
    >>> motor.acelerar()
    >>> motor.frear()
    >>> motor.frear()
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao=direcao, motor=motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'

'''
from direcao import Direcao
from motor import Motor

class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        self.motor.calcular_velocidade()

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def calcular_direcao(self):
        return self.direcao.calcular_direcao()


mot = Motor()
dir = Direcao()

car = Carro(motor=mot, direcao=dir)
car.girar_a_direita()
car.calcular_direcao()
