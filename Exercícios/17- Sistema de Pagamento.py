from abc import ABC, abstractmethod
from datetime import datetime
class Pagamento(ABC):
    def __init__(self, quantia: float, data: str) -> None:
        if quantia > 0:
            self.quantia = quantia
            self.data = data
        else:
            print('Pagamento não efetuado! Digite um valor válido!')

    @abstractmethod
    def efetuar_pagamento(self):
        pass

class Dinheiro(Pagamento):
    def __init__(self, quantia: float, data: str, moeda: str) -> None:
        super().__init__(quantia, data)
        self.moeda = moeda
    
    def efetuar_pagamento(self, dinheiro_recebido: float):
        if dinheiro_recebido < self.quantia:
            print('Pagamento no dinheiro não efetuado! Saldo insuficiente!')
        else:
            troco = dinheiro_recebido - self.quantia
            print(f'Pagamento no dinheiro concluído! Seu troco é de: R$ {troco:.2f}')

class CartaoCredito(Pagamento):
    def __init__(self, quantia: float, data: str, num_cartao: int, validade: str, limite: float) -> None:
        super().__init__(quantia, data)
        self.num_cartao = num_cartao
        self.validade = validade
        self.limite = limite
    
    def efetuar_pagamento(self):
        data_formatada = datetime.strptime(self.data[3:], '%m/%Y')
        validade_formatada = datetime.strptime(self.validade, '%m/%Y')

        if validade_formatada >= data_formatada:
            if self.quantia > self.limite:
                print('Limite do cartão atingido!')
            else:
                print(f'Pagamento no cartão concluído! R$ {self.quantia:.2f}')
        else:
            print('Cartão está fora da validade!')

class Cheque(Pagamento):
    def __init__(self, quantia: float, data: str, num_cheque: int, banco: str, saldo_conta: float) -> None:
        super().__init__(quantia, data)
        self.num_cheque = num_cheque
        self.banco = banco
        self.saldo_conta = saldo_conta

    def efetuar_pagamento(self):
        if len(self.num_cheque) == 6 and self.num_cheque.isdigit():
            print('Cheque aprovado!')
            if self.saldo_conta > self.quantia:
                print(f'Pagamento no cheque concluído! R$ {self.quantia:.2f}')
            else:
                print('Saldo insuficiente!')
        else:
            print('Cheque inválido!')

def main():
    dinheiro1 = Dinheiro(50.00, '01/02/2024', 'Real')
    dinheiro1.efetuar_pagamento(60.00)

    dinheiro2 = Dinheiro(70.00, '02/02/2024', 'Real') 
    dinheiro2.efetuar_pagamento(40.00) # Saldo insuficiente

    cartao1 = CartaoCredito(97.50, '03/02/2024', 123456789, '05/2025', 100.00)
    cartao1.efetuar_pagamento()

    cartao2 = CartaoCredito(200.00, '04/02/2023', 987654321, '05/2025', 150.00)
    cartao2.efetuar_pagamento() # Limite atingido

    cartao3 = CartaoCredito(160.00, '03/01/2024', 374329472, '12/2023', 200.00)
    cartao3.efetuar_pagamento() # Fora da validade

    cheque1 = Cheque(270.00, '20/01/2024', '123456', 'Itaú', 300.00)
    cheque1.efetuar_pagamento() 

    cheque2 = Cheque(120.00, '30/01/2024', '274939', 'Bradesco', 90.00)
    cheque2.efetuar_pagamento() # Saldo insuficiente

    cheque3 = Cheque(60.00, '25/01/2024', 'ABC123', 'Santander', 80.00)  # Deve imprimir 'Cheque inválido!'
    cheque3.efetuar_pagamento() # Cheque inválido

    dinheiro3 = Dinheiro(0.00, '26/01/2024', 'Dólar') # Não efetuado
    dinheiro3 = Dinheiro(-10.00, '28/01/2024', 'Euro') # Não efetuado

if __name__ == '__main__':
    main()