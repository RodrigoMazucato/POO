class Livro:
    def __init__(self, titulo: str, autor: str, ano_publicacao: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano_publicacao

    def mostrar_info(self) -> str:
        return f'{self.titulo} | Autor: {self.autor} | Ano: {self.ano}'

class Biblioteca:
    def __init__(self, capacidade: int) -> None:
        self.livros = []
        self.capacidade = capacidade

    def adicionar_livros(self, livro: Livro) -> None:
        contagem = f'({len(self.livros)+1}/{self.capacidade})'
        if len(self.livros) < self.capacidade:
            self.livros.append(livro)
            print(f'Livro adicionado com sucesso! {contagem}')
        else:
            print(f'Não é possível adicionar mais livros! A capacidade máxima da biblioteca foi atingida! {contagem}')

    def mostrar_livros(self) -> None:
        for num, livro in enumerate(self.livros, start=1):
            print(f'{num}- {livro.mostrar_info()}')

def main():
    livro1 = Livro('Harry Potter', 'J. K. Rowling', 1997)
    livro2 = Livro('Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
    livro3 = Livro('Orgulho e Preconceito', 'Jane Austen', 1813)
    livro4 = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943)
    livro5 = Livro('Dom Quixote', 'Miguel de Cervantes', 1605)
    livro6 = Livro('A Revolução dos Bichos', 'George Orwell', 1945)

    biblioteca = Biblioteca(5)
    biblioteca.adicionar_livros(livro1)
    biblioteca.adicionar_livros(livro2)
    biblioteca.adicionar_livros(livro3)
    biblioteca.adicionar_livros(livro4)
    biblioteca.mostrar_livros()
    biblioteca.adicionar_livros(livro5)
    biblioteca.mostrar_livros()
    biblioteca.adicionar_livros(livro6)
main()