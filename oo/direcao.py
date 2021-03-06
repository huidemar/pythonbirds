'''
A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:

1 - Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
2 - Método girar_a_direita
3 - Método girar_a_esquerda
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
'''
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