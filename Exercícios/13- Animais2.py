from abc import ABC, abstractmethod
class Animal:
    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome
    
    @property
    def idade(self) -> int:
        return self.__idade
    
    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    def get_qtd_comida(self, qtd_dias: int) -> None:
        tipo = type(self).__name__.lower()
        n = self.qtd_alimento * qtd_dias
        return f"{self.x} {tipo} {self.nome.lower()} come {n}{self.medida} de alimento em {qtd_dias} {'dia' if qtd_dias == 1 else 'dias'}."

class Mamifero(Animal):
    x = 'O'
    qtd_alimento = 2
    medida = 'kg'

class Peixe(Animal):
    x = 'O'
    qtd_alimento = 100
    medida = 'g'

class Ave(Animal):
    x = 'A'
    qtd_alimento = 20
    medida = 'g'
    
mamifero = Mamifero('Cachorro', 4)
print(f'Nome: {mamifero.nome} | Idade: {mamifero.idade}')
print(mamifero.get_qtd_comida(3))

mamifero.idade = 5
print(f'Nome: {mamifero.nome} | Idade: {mamifero.idade}')

peixe = Peixe('Golfinho', 10)
print(f'Nome: {peixe.nome} | Idade: {peixe.idade}')
print(peixe.get_qtd_comida(4))

ave = Ave('Águia', 12)
print(f'Nome: {ave.nome} | Idade: {ave.idade}')
print(ave.get_qtd_comida(10))
