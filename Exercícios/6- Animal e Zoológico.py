class Animal:
    def __init__(self, nome: str, especie: str, idade: int) -> None:
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def mostrar_info(self) -> None:
        return f'{self.nome} | Espécie: {self.especie} | Idade: {self.idade}'

class Zoologico:
    def __init__(self, capacidade: int) -> None:
        self.animais = []
        self.capacidade = capacidade

    def adicionar_animal(self, animal: Animal) -> None:
        contagem = f'({len(self.animais)+1}/{self.capacidade})'
        if len(self.animais) < self.capacidade:
            self.animais.append(animal)
            print(f'Animal inserido com sucesso! {contagem}')
        else:
            print(f'Não é possível adicionar mais animais! O Zoológico já atingiu a capacidade máxima! {contagem}')

    def mostrar_animais(self) -> None:
        for num, animal in enumerate(self.animais, start=1):
            print(f'{num}- {animal.mostrar_info()}')

if __name__ == '__main__':
    animal1 = Animal('Spike', 'Tigre', 15)
    animal2 = Animal('Thor', 'Leão', 20)
    animal3 = Animal('Cláudia', 'Raia', 10)
    animal4 = Animal('Bruno', 'Sapo', 12)
    animal5 = Animal('Pedro', 'Pinguim', 9)

    zoo = Zoologico(4)
    zoo.adicionar_animal(animal1)
    zoo.adicionar_animal(animal2)
    zoo.adicionar_animal(animal3)
    zoo.mostrar_animais()
    zoo.adicionar_animal(animal4)
    zoo.adicionar_animal(animal5)
    zoo.mostrar_animais()