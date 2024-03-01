import random
import time

def jogar(resultado):
    opcoes = ['pedra', 'papel', 'tesoura']
    while True:
        usuario = input('Pedra, papel ou tesoura? ')
        if usuario.lower() not in opcoes:
            print('Digite uma opção válida!')
        else:
            break
    maquina = random.choice(opcoes)
    print('Máquina: ', end='')
    time.sleep(1)
    print(maquina)
    time.sleep(1)
    print('-' * 35)
    if (usuario == 'pedra' and maquina == 'tesoura') or \
       (usuario == 'papel' and maquina == 'pedra') or \
       (usuario == 'tesoura' and maquina == 'papel'):
        print('Você ganhou!')
        resultado['vitoria'] += 1
        
    elif usuario == maquina:
        print('Você empatou!')
        resultado['empate'] += 1
        
    else:
        print('Você perdeu!')
        resultado['derrota'] += 1
        
    print('-' * 35)

def exibir_placar(resultado):
    print('-' * 35)
    print('Resultado final: ')
    print('-' * 35)
    print(f"Vitórias: {resultado['vitoria']}")
    print(f"Empates: {resultado['empate']}")
    print(f"Derrotas: {resultado['derrota']}")
    print('-' * 35)

def main():
    resultado = {'vitoria': 0, 'empate': 0, 'derrota': 0}
    print('-' * 35)
    print(f"{'Jogo do Jokenpô!':^35}")
    print('-' * 35)
    while True:
        jogar(resultado)
        x = input('Deseja jogar novamente (s/n)? ')
        if x.lower() in ['nao', 'não', 'n']:
            exibir_placar(resultado)
            break
main()
