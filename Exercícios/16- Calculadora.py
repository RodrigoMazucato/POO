from abc import ABC, abstractmethod

class CampoVazioError(Exception):
    pass

class Calculadora(ABC):
    @abstractmethod
    def calcular(self, a: float, b: float) -> str:
        pass

class Soma(Calculadora):
    def calcular(self, a: float, b: float) -> None:
        print(f'Soma: {a} + {b} = {a + b}')
    
class Subtracao(Calculadora):
    def calcular(self, a: float, b: float) -> None:
        print(f'Subtração: {a} - {b} = {a - b}')
    
class Multiplicacao(Calculadora):
    def calcular(self, a: float, b: float) -> None:
        print(f'Multiplicação: {a} x {b} = {a * b}')
    
class Divisao(Calculadora):
    def teste_vazio(self, a: any, b: any) -> None:
        if a == '' or b == '':
            raise CampoVazioError
        
    def calcular(self, a: float, b: float) -> str:
        try:
            self.teste_vazio(a,b)
            resultado = a / b
        except ZeroDivisionError:
            print('Não é possível dividir por zero!')
        except TypeError:
            print('Operação inválida!')
        except CampoVazioError:
            print('O campo não pode ficar vazio!')
        else:
            print(f'Divisão: {a} / {b} = {a / b}')
        finally:
            print('Fim de operação!')

def main():
    soma = Soma()
    soma.calcular(3, 4)

    subtracao = Subtracao()
    subtracao.calcular(5, 2)

    mult = Multiplicacao()
    mult.calcular(4, 6)

    div = Divisao()
    div.calcular(10, 2)
    div.calcular(10, 0)
    div.calcular('',10)
main()