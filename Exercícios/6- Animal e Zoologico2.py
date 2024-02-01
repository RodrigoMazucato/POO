class DadosVazios(Exception):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    def __str__(self) -> str:
        return f"O Campo: {self.mensagem} não é permitido valor vazio!"

class Animal:
    lista = []
    capacidade = 5
    def __init__(self, nome: str, especie: str, idade: int) -> None:
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.__adicionar_animal()

    def __adicionar_animal(self):
        if len(self.lista) < self.capacidade:
          Animal.lista.append(self)
      
    # representação dos atributos
    def __repr__(self) -> str:
        return f"{self.nome}, {self.especie}, {self.idade}"
    
    @classmethod
    def mostrar_animais(cls) -> None: # recebe a classe inteira (Animal.lista)
        for animal in cls.lista:
            print(animal)

animal1 = Animal('Leao', 'mamifero', 25)
animal2 = Animal('Tigre', 'mamifero', 15)
animal3 = Animal('Vaca', 'mamifero', 20)
animal4 = Animal('Golfinho', 'mamifero', 30)
animal5 = Animal('Golfinho', 'mamifero', 30)
animal6 = Animal('Golfinho', 'mamifero', 30)

Animal.mostrar_animais()

# para erro 
# animal4 = Animal("nome", "", 30)