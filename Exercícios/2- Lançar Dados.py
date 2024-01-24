import time
import random

def sortear(a,b):
    return random.randint(a,b)

def lancar_dado(jogador):
    for _ in range(sortear(5,21)):
        print(sortear(1,6), end=' ')
        time.sleep(0.1)
        
    print(f'\n{jogador}: ', end='')
    time.sleep(0.5)
    num = random.randint(1,6)
    print(num)
    return num

def jogar(resultado):
    input('Aperte ENTER para lançar o dado... ')
    usuario = lancar_dado('Seu número')    
    maquina = lancar_dado('Máquina')
    time.sleep(1)
    print('-' * 35)
    if usuario > maquina:
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
    print(f"{'Jogo dos dados!':^35}")
    print('-' * 35)
    while True:
        jogar(resultado)
        escolha = input('Deseja jogar novamente (s/n)? ')
        if escolha.lower() in ['nao', 'não', 'n']:
            exibir_placar(resultado)
            break
main()
    
