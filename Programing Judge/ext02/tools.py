class pessoa:
    def __init__(self, nome, idade, sexo, emocional):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.emocional = emocional
    
    def status(self, nome):
        if self.nome == nome:
            print(f'''\033[1;36m
            Nome: {self.nome}
            Idade: {self.idade}
            Sexo: {self.sexo}
            Estatus Emocional: {self.emocional}
            ''')
        else:
            print('\033[1;31mEsse nome não está atribuído a classe atual!')
