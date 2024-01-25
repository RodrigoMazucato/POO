from abc import ABC, abstractmethod
class Calculadora(ABC):
    def __init__(self, usuario: str) -> None:
        self.__usuario = usuario
    
    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, novo):
        self.__usuario = novo

    @abstractmethod
    def calcular(self, a, b):
        pass

class Soma(Calculadora):
    def calcular(self, a: float, b: float) -> str:
        return f'Soma: {a} + {b} = {a + b}'
    
class Subtracao(Calculadora):
    def calcular(self, a: float, b: float) -> str:
        return f'Subtração: {a} - {b} = {a - b}'
    
class Multiplicacao(Calculadora):
    def calcular(self, a: float, b: float) -> str:
        return f'Multiplicação: {a} x {b} = {a * b}'
    
class Divisao(Calculadora):
    def teste_vazio(self, a: any, b: any) -> None:
        if a == '' or b == '':
            raise TypeError
        
    def calcular(self, a: float, b: float) -> str:
        try:
            self.teste_vazio(a,b)
            resultado = a / b
        except ZeroDivisionError:
            print('Não pode dividir por zero!')
        except TypeError:
            print('Operação inválida!')
        else:
            print('Divisão: {a} / {b} = {a / b}')
        finally:
            print('Fim de operação!')