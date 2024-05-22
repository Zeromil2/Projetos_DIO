class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print(f'Removendo a instância da classe.{self.nome}')

    def falar(self):
        print('auau')


def criar_cachorro():
    dog2 = Cachorro('Pluto', 'amarelo', False)
    print(dog2.nome)

dog1 = Cachorro('Bolt', 'branco')
dog1.falar()

criar_cachorro()

print('Olá, Mundo!')

del dog1

print('Olá, mundo!')
