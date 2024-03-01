from random import randint
from time import sleep

def mostrar_menu():
    print(f"{'-' * 35}\nGerenciador Simples de Tarefas\n{'-' * 35}")
    print('1- Adicionar Tarefa')
    print('2- Visualizar Tarefas')
    print('3- Remover Tarefa')
    print('4- Sair')

def main():
    tarefas = {}
    while True:
        mostrar_menu()
        try:
            escolha = int(input('Escolha uma opção: '))
        except ValueError:
            print('Digite um número inteiro!')
            continue
        
        match escolha:
            case 1:
                descricao = input('Insira a descrição da tarefa: ')
                if descricao in tarefas.values():
                    print('-' * 35)
                    print('Tarefa já cadastrada!')
                else:
                    while True:
                        chave = randint(1000, 9999)
                        if chave not in tarefas.keys(): # para não ter número repetido
                            break
                        if len(tarefas) == len(range(1000, 9999+1)):
                            print('Limite máximo alcançado!')
                            quit()

                    tarefas[chave] = descricao
                    print('Tarefa adicionada com sucesso!')
                    print('-' * 35)
                    print(f'{chave}: {tarefas[chave]}')

            case 2:
                if len(tarefas) == 0: # tarefas == {}
                    print('-' * 35)
                    print('Nenhuma tarefa cadastrada!')
                else:
                    lista_chaves = sorted(tarefas) # ou tarefas.keys()
                    print('-' * 35)
                    for indice, chave in enumerate(lista_chaves, start=1):
                        print(f'{indice}- {chave}: {tarefas[chave]}')

            case 3:
                while True:
                    try:
                        chave = int(input('Digite o id da tarefa: '))
                    except ValueError:
                        print('Digite um número válido!')
                    else:
                        break

                if chave in tarefas.keys():
                    del tarefas[chave]
                    print('Tarefa removida com sucesso!')
                else:
                    print('Chave não encontrada!')

            case 4:
                opcao = input('Deseja mesmo sair do programa? (s/n) ')
                if opcao.lower() not in ['n', 'nao', 'não']:
                    print('Saindo do programa...')
                    sleep(1)
                    break

            case _:
                print('Opção inválida!')

        print('-' * 35)
        input('Pressione ENTER para continuar...')        
main()