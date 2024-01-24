class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.status = 'disponível'
        biblioteca.livros.append(self)

    def emprestar(self) -> None:
        self.status = 'emprestado'

    def devolver(self) -> None:
        self.status = 'disponível'

    def ver_info(self) -> None:
        return f'{self.titulo} | Autor: {self.autor} | ISBN: {self.isbn} | Status: {self.status}'

class Usuario:
    def __init__(self, nome: str, id: int) -> None:
        self.nome = nome
        self.id = id
        self.livros_emprestados = []
        biblioteca.usuarios.append(self)

    def emprestar_livro(self, livro: Livro) -> None:
        contagem = f'({len(self.livros_emprestados)+1}/{biblioteca.limite})'
        if len(self.livros_emprestados) < biblioteca.limite:
            self.livros_emprestados.append(livro)
            livro.emprestar()
            print(f'O livro \'{livro.titulo}\' foi emprestado com sucesso pelo(a) {self.nome}! {contagem}')
        else:
            print(f'Você já atingiu o limite! {contagem}')

    def devolver_livro(self, livro: Livro) -> None:
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.devolver()
            print(f'O livro \'{livro.titulo}\' foi devolvido com sucesso!')
        else:
            print('Esse livro não foi emprestado!')

    def ver_info(self)-> str:
        return f'{self.id} | {self.nome}'
    
    def ver_livros_emprestados(self):
        if len(self.livros_emprestados) == 0:
            print(f'O(A) {self.nome} não pegou nenhum livro emprestado!')
        else:
            print('-' * 90)
            print(f'Livros emprestados do(a) {self.nome}:')
            print('-' * 90)
            for indice, livro in enumerate(self.livros_emprestados, start=1):
                print(f'{indice}- {livro.ver_info()}')
            print('-' * 90)

class Biblioteca:
    def __init__(self, limite: int) -> None:
        self.livros = []
        self.usuarios = []
        self.limite = limite

    def listar_livros(self) -> None:
        print('-' * 90)
        print('Livros:')
        print('-' * 90)
        if len(self.livros) == 0:
            print('Nenhum livro cadastrado!')
        else:
            for livro in self.livros:
                print(f'- {livro.ver_info()}')
        print('-' * 90)

    def listar_usuarios(self) -> None:
        print('-' * 20)
        print('Usuários:')
        print('-' * 20)
        if len(self.usuarios) == 0:
            print('Nenhum usuário cadastrado!')
        else:
            for usuario in self.usuarios:
                print(usuario.ver_info())
        print('-' * 20)

    def pesquisar_livro(self, termo: str) -> None:
        for livro in self.livros:
            if termo in [livro.titulo, livro.autor, livro.isbn]:
                print(f'- {livro.ver_info()}')
                return
        print('Livro não encontrado!')
        
    def pesquisar_usuario(self, termo):
        for usuario in self.usuarios:
            if termo in [usuario.nome, usuario.id] :
                print(usuario.ver_info())
                print(usuario.ver_livros_emprestados())
                return
        print('Usuário não encontrado!')

if __name__ == '__main__':
    biblioteca = Biblioteca(limite=3)
    livro1 = Livro('Harry Potter', 'J. K. Rowling', '978-3-16-148410-0')
    livro2 = Livro('Orgulho e Preconceito', 'Jane Austen', '978-1-78184-010-2')
    livro3 = Livro('Dom Casmurro', 'Machado de Assis', '978-8-53804-192-5')
    livro4 = Livro('A hora da estrela', 'Clarice Lispector', '978-8-53250-812-6')
    biblioteca.listar_livros()
    usuario1 = Usuario('Rodrigo', 1234)
    usuario2 = Usuario('Guilherme', 5678)
    biblioteca.listar_usuarios()
    usuario1.emprestar_livro(livro1)
    usuario2.emprestar_livro(livro2)
    usuario1.ver_livros_emprestados()
    biblioteca.listar_livros()
    biblioteca.pesquisar_livro("Harry Potter")
    biblioteca.pesquisar_livro("ABDC")
    biblioteca.pesquisar_usuario("Guilherme")
    biblioteca.pesquisar_usuario("Alessandro")
    usuario1.devolver_livro(livro1)
    usuario2.emprestar_livro(livro3)
    usuario2.emprestar_livro(livro4)
    usuario2.emprestar_livro(livro1)
    usuario2.ver_livros_emprestados()
    usuario2.devolver_livro('ABCD')
    biblioteca.listar_livros()
    
    # biblioteca = Biblioteca()

    # livro1 = Livro()
    # livro2 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', '978-0-544-22785-2')
    # livro3 = Livro('Orgulho e Preconceito', 'Jane Austen', '978-1-78184-010-2')
    # livro4 = Livro('Dom Quixote', 'Miguel de Cervantes', '978-1-56619-909-4')

    # usuario = Usuario('Rodrigo', 1234, 3)
    # usuario.emprestar_livro(livro1)
    # livro1.ver_info()
    # livro2.ver_info()
    # usuario.emprestar_livro(livro2)
    # livro2.ver_info()
    # usuario.emprestar_livro(livro3)
    # livro3.ver_info()
    # usuario.emprestar_livro(livro4)
    # usuario.devolver_livro(livro1)
    # livro1.ver_info()
