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

    @abstractmethod
    def get_qtd_comida(self) -> None:
        pass

class Mamifero(Animal):
    qtd_kg = 2
    def get_qtd_comida(self, qtd_dias: int) -> str:
        return f"O mamífero {self.nome.lower()} come {self.qtd_kg * qtd_dias}kg de alimento em {qtd_dias} {'dia' if qtd_dias == 1 else 'dias'}."

class Peixe(Animal):
    qtd_gramas = 100
    def get_qtd_comida(self, qtd_dias: int) -> str:
        return f"O peixe {self.nome.lower()} come {self.qtd_gramas * qtd_dias}g de alimento em {qtd_dias} {'dia' if qtd_dias == 1 else 'dias'}."

class Ave(Animal):
    qtd_gramas = 20
    def get_qtd_comida(self, qtd_dias: int) -> str:
        return f"A ave {self.nome.lower()} come {self.qtd_gramas * qtd_dias}g de alimento em {qtd_dias} {'dia' if qtd_dias == 1 else 'dias'}."
    
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
