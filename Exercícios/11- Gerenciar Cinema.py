class Filme:
    def __init__(self, nome: str, duracao: int, classificacao: str) -> None:
        self.__nome = nome
        self.__duracao = duracao
        self.__classificacao = classificacao

    def __repr__(self):
        return f'{self.__nome} | Duração: {self.__duracao} minutos | Classificacao: {self.__classificacao}'

class Sala:
    def __init__(self, capacidade: int, filme: Filme) -> None:
        self.__capacidade = capacidade
        self.__filme = filme
    
    @property
    def filme(self):
        return self.__filme
    
    @filme.setter
    def filme(self, novo_filme: Filme) -> None:
        if novo_filme == self.__filme:
            print('Esse filme já está sendo reproduzido!')
        else:
            self.__filme = novo_filme
            print('Filme alterado com sucesso!')

    def verificar_capacidade(self) -> str:
        return f'Capacidade da sala: {self.__capacidade} {'pessoa' if self.__capacidade == 1 else  'pessoas'}'
    
filme1 = Filme('Beethoven', 87, 'Livre')
filme2 = Filme('Barbie', 114, '+ 12 anos')

sala = Sala(45, filme1)
print(sala.filme)
sala.filme = filme2
print(sala.filme)
sala.filme = filme2
print(sala.verificar_capacidade())

sala2 = Sala(1, filme1)
print(sala2.verificar_capacidade())