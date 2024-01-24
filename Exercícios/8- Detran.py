from datetime import datetime
class Carteira:
    def __init__(self, numero: int, cpf: str, tipo: str, data_validade: str, data_expedicao: str) -> None:
        self.numero = numero
        self.cpf = cpf
        self.tipo = tipo
        self.data_validade = data_validade
        self.data_expedicao = data_expedicao
        self.pontos = 0
        self.situacao = 'válida'
    
    def acrescentar_pontos(self, infracao: str) -> None:
        match infracao.lower():
            case 'leve':
                self.pontos += 3

            case 'media' | 'média':
                self.pontos += 4

            case 'grave':
                self.pontos += 5

            case 'gravissima' | 'gravíssima':
                self.pontos += 7

        if self.pontos >= 20:
            self.situacao = 'apreendida'
            print(f'Sua carteira foi apreendida! ({self.pontos} pontos)')

    def consultar_pontos(self) -> None:
        print(f'{self.pontos} pontos')
    
    def zerar_pontos(self, pagou_multa: str) -> None:
        if pagou_multa.lower() in ['sim', 's']:
            self.pontos = 0
            self.situacao = 'válida'
            print('Sua carteira foi zerada!')
        else:
            print('Sua carteira não foi zerada! Page a multa primeiro!')

    def verificar_situacao(self) -> None:
        validade = datetime.strptime(self.data_validade, '%d/%m/%Y')
        if validade < datetime.now():
            self.situacao = 'vencida'
        print(f'A carteira está {self.situacao}.')
    
if __name__ == '__main__':
    carteira = Carteira(123456789, '987-654-321.00', 'B', '20/01/2025', '20/01/2020')

    carteira.acrescentar_pontos('média')
    carteira.consultar_pontos()
    carteira.acrescentar_pontos('gravíssima')
    carteira.consultar_pontos()
    carteira.acrescentar_pontos('grave')
    carteira.consultar_pontos()
    carteira.verificar_situacao()

    carteira.acrescentar_pontos('leve')
    carteira.consultar_pontos()

    carteira.acrescentar_pontos('leve')
    carteira.verificar_situacao()

    carteira.zerar_pontos('não')
    carteira.zerar_pontos('sim')

    carteira.verificar_situacao()
    carteira.consultar_pontos()
    print('-' * 25)

    carteira2 = Carteira(765891432, '726-938-173.44', 'AB', '01/01/2024', '01/01/2019')
    carteira2.verificar_situacao()
    carteira.consultar_pontos()