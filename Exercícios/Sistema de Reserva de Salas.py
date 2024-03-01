from time import sleep
salas = {}
for letra in 'ABCDE':
    salas[letra] = 'Disponível'

def mostrar_menu():
    print(f"{'-' * 35}\nSistema de Reserva de Salas\n{'-' * 35}")
    print('1- Listar salas disponíveis')
    print('2- Reservar uma sala')
    print('3- Cancelar reserva de uma sala')
    print('4- Sair')

def main():
    while True:
        mostrar_menu()
        try:
            escolha = int(input('Escolha uma opção: '))
        except ValueError:
            print('Digite um número inteiro!')
            continue
        
        match escolha:
            case 1:
                print('-' * 35)
                for chave, valor in salas.items():
                    print(f'Sala {chave}: {valor}')
            case 2:
                disp = []
                for chave, valor in salas.items():
                    if valor == 'Disponível':
                        disp.append(chave)

                if len(disp) == 0:
                    print('Nenhuma sala disponível! Cancele alguma reseva!')
                else:
                    escolha = input(f"Qual sala deseja reservar? ({'/'.join(disp)}) ").upper()
                    if escolha in salas.keys():
                        if salas[escolha] == 'Disponível':
                            salas[escolha] = 'Reservado'
                            print(f'\'Sala {escolha}\' reservada com sucesso!')
                        else:
                            print('Sala não disponível!')
                    else:
                        print('Sala não cadastrada!')

            case 3:
                reservadas = []
                for chave, valor in salas.items():
                    if valor == 'Reservado':
                        reservadas.append(chave)

                if len(reservadas) == 0:
                    print('Nenhuma sala reservada! Faça alguma reseva!')
                else:
                    escolha = input(f"Qual reserva deseja cancelar? ({'/'.join(reservadas)}) ").upper()
                    if escolha in salas.keys():
                        if salas[escolha] == 'Reservado':
                            salas[escolha] = 'Disponível'
                            print(f'A reserva da sala {escolha} foi cancelada com sucesso!')
                        else:
                            print('Sala não reservada!')
                    else:
                        print('Sala não cadastrada!')

            case 4:
                opcao = input('Deseja mesmo sair do programa? (s/n) ')
                if opcao.lower() not in ['n', 'nao', 'não']:
                    print('Saindo do programa...')
                    sleep(1)
                    break

            case _:
                print('Opção inválida!')

        print('-' * 35)
        input('Pressione ENTER para continuar... ')        
main()