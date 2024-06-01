class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim... Plim...")

    def parar(self):
        print("Parando bicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vruuummm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


bike1 = Bicicleta("amarela", "Naruto", 2003, 500)
bike1.parar()
bike1.correr()
bike1.buzinar()
print(bike1.cor, bike1.modelo, bike1.ano, bike1.valor)

bike2 = Bicicleta("vermelha", "Pucca", 2000, 200)
print(bike2)
bike2.correr()
