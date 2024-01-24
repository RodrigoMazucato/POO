class Animal:
    def __init__(self, nome, tipo, som):
        self.nome = nome
        self.tipo = tipo
        self.som = som

    def setSom(self, som):
        self.som = som

    def fazerSom(self):
        print(f'{self.nome} faz {self.som}!')
    
    def alimentar(self):
        print(f'Dando ração para o(a) {self.tipo} {self.nome}!')

    def dormir(self):
        print(f'{self.nome} está dormindo!')

    def mostrarInfo(self):
        print(f'Nome: {self.nome} | Tipo: {self.tipo} | Som: {self.som}')

class Animal2:
    def __init__(self, nome, tipo, som):
        self.nome = nome
        self.tipo = tipo
        self.__som = som

    @property
    def som(self):
        return self.__som

    @som.setter
    def som(self, som):
        self.__som = som

    def __repr__(self):
        return f'Nome: {self.nome} | Tipo: {self.tipo} | Som: {self.__som}'

a1 = Animal('Yuki', 'cachorro', 'au au')
a2 = Animal('Matilda', 'gata', 'miau')
a3 = Animal('Clotilde', 'galinha', 'cocó')