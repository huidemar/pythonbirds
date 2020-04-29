class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=100):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá meu nome é {}'.format(self.nome)

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_class(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão!'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    ticio = Mutante(nome='Tício')
    mevio = Homem(ticio, nome='Mévio')
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
    print(Pessoa.metodo_estatico(),mevio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_class(), mevio.nome_e_atributos_de_class())
    fulano = Pessoa(nome='Anonimo')
    print(isinstance(fulano, Pessoa))
    print(isinstance(fulano, Homem))
    print(isinstance(mevio, Pessoa))
    print(isinstance(mevio, Homem))
    print(ticio.olhos)
    print(ticio.cumprimentar())
    print(mevio.cumprimentar())