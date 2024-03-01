import time
def maximo(lista):
    tamanhos = []
    for item in lista:
        tamanhos.append(len(item))
    return max(tamanhos)

arquivo = open('biblioteca.txt', 'a')

livros = []
emprestimos = {}
while True:
    print('-'* 53)
    print('EMPRÉSTIMO DE LIVROS')
    print('-'* 53)
    print(f'1- Adicionar livro | 4- Ver empréstimos    | 7- Sair')
    print(f'2- Listar livro    | 5- Devolução de livro | ')
    print(f'3- Emprestar livro | 6- Pesquisar livro    | ')
    escolha = int(input('\nEscolha uma opção: '))
    match escolha:
        case 1:
            titulo = input('Digite o título do livro: ')
            if titulo in livros:
                print('O livro já foi cadastrado.')
            else:
                livros.append(titulo)
                print('Livro cadastrado com sucesso!')
                      
        case 2:
            if livros == []:
                print('Nenhum livro cadastrado!')
            else:
                print('Livros disponíveis:')
                for livro in livros:
                    print(f'- {livro}')

        case 3:
            tit_emp = input('Digite o livro que deseja pegar emprestado: ')
            if tit_emp in livros:
                if tit_emp in emprestimos:
                    print('Livro já emprestado!')
                else:
                    leitor = input('Digite o nome do leitor: ')
                    emprestimos[tit_emp] = leitor
                    print('Empréstimo realizado com sucesso!')
            else:
                print('Esse livro não foi cadastrado!')

        case 4:
            # max_livro = max(len(livro) for livro in emprestimos.keys())
            # max_leitor = max(len(leitor) for leitor in emprestimos.values())
            if emprestimos == {}:
                print('Nenhum empréstimo realizado!')
            else:
                print('Livros emprestados: ')
                k = maximo(emprestimos.keys())
                v = maximo(emprestimos.values())
                for livro, leitor in emprestimos.items():
                    print(f'- Livro: {livro:{k}} | Leitor: {leitor:{v}} |')

        case 5:
            devolve = input('Digite o livro a ser devolvido: ')
            if devolve in livros:
                if devolve in emprestimos.keys():
                    del emprestimos[devolve]
                    print('Livro devolvido com sucesso!')
                else:
                    print('Livro não emprestado!')
            else:
                print('Livro não cadastrado!')
                
        case 6:
            pesquisa = input('Digite o livro a ser pesquisado: ')
            if pesquisa in livros:
                print('Livro encontrado!')
            else:
                print('Livro não encontrado!')
                
        case 7:
            arquivo.write('\nLivros: \n')
            for livro in livros:
                arquivo.write(f'- {livro}\n')
                
            arquivo.write('\nEmpréstimos: \n')
            for livro, leitor in emprestimos.items():
                arquivo.write(f"'{livro}': {leitor}\n")
                
            arquivo.write('-' * 25)
            arquivo.close()
            print('Saindo...')
            time.sleep(1)
            break

        case _:
            print('Opção inválida!')
    print('-' * 53)
    input('Pressione ENTER para continuar...')