class Pessoa:

    def __init__(self, nome=None, idade=100):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return 'Olá {}'.format(id(self))


if __name__ == '__main__':
    p = Pessoa('Tício')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Huidemar'
    print(p.nome)
    print(p.idade)

