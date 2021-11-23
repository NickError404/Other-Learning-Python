'''
Você irá criar a class Carro e eu quero no mínimo 3 propriedades para a classe carro e no mínimo 3 métodos para ela
'''


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print('\033[1;32mLigando...')

    def desligar(self):
        print('\033[1;31mDesligando...')

    def informações(self):
        print(f'\033[1;36mModelo: {self.modelo}\nMarca: {self.marca}\nAno: {self.ano}')


carro1 = Carro('Ferrari', 'FXX EVOLUZIONE', 1940)

carro1.ligar()
carro1.desligar()
carro1.informações()
