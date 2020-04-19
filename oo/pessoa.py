class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=100):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá {}'.format(id(self))


if __name__ == '__main__':
    ticio = Pessoa(nome='Tício')
    mevio = Pessoa(ticio, nome='Mévio')
    print(Pessoa.cumprimentar(mevio))
    print(id(mevio))
    print(mevio.cumprimentar())
    print(mevio.nome)
    print(mevio.idade)
    for filho in mevio.filhos:
        print(filho.nome)

    mevio.sobrenome = 'Kifure'  #criando atributo dinamico
    del mevio.filhos  #remove os atributos dinamicamente
    mevio.olhos = 1
    print(mevio.__dict__)
    print(ticio.__dict__)
    print(Pessoa.olhos)
    print(mevio.olhos)
    print(ticio.olhos)
    print(id(Pessoa.olhos), id(mevio.olhos), id(ticio.olhos))

