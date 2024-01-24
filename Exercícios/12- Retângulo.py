class Retangulo:
    def __init__(self, largura: float, comprimento: float):
        if largura > 0 and comprimento > 0:
            self.largura = largura
            self.comprimento = comprimento
        else:
            print('A largura e o comprimento precisam ser maiores que 0!')

    def calcular_perimetro(self):
        return f'Perímetro: {(self.largura + self.comprimento) * 2}'
        
    def calcular_area(self):
        return f'Área: {self.largura * self.comprimento}'

r1 = Retangulo(4.5, 10)
print(r1.calcular_perimetro())
print(r1.calcular_area())
r2 = Retangulo(-1, 20)