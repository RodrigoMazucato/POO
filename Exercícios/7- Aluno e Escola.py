class Aluno:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def mostrar_info(self) -> None:
        return f'{self.nome} | Idade: {self.idade}'

class Escola:
    def __init__(self, capacidade: int) -> None:
        self.alunos = []
        self.capacidade = capacidade

    def adicionar_aluno(self, aluno: Aluno) -> None:
        contagem = f'({len(self.alunos)+1}/{self.capacidade})'
        if len(self.alunos) < self.capacidade:
            self.alunos.append(aluno)
            print(f'Aluno inserido com sucesso! {contagem}')
        else:
            print(f'Não é possível adicionar mais alunos! A capacidade máxima da escola já foi atingida! {contagem}')

    def mostrar_alunos(self) -> None:
        alunos = sorted(self.alunos, key= lambda aluno: aluno.nome)
        print('-' * 25)
        print('Lista de Alunos:')
        print('-' * 25)
        for num, aluno in enumerate(alunos, start=1):
            print(f'{num}- {aluno.mostrar_info()}')
        print('-' * 25)

if __name__ == '__main__':
    dados = [('André', 12), ('Lucas', 14), ('Gustavo', 13),
    ('Enzo', 15), ('Heloísa', 12), ('Letícia', 16)]

    escola = Escola(5)
    for nome, idade in dados:
        escola.adicionar_aluno(Aluno(nome, idade))
        
    escola.mostrar_alunos()