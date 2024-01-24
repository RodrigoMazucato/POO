class Carro:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__ligado = False

    def ligar(self):
        if self.__ligado == True:
            print('O carro já está ligado!')
        else:
            self.__ligado = True
            print('O carro foi ligado!')

    def desligar(self):
        if self.__ligado == False:
            print('O carro já está desligado!')
        else:
            self.__ligado = False
            print('O carro foi desligado!')

    def mostrarInfo(self):
        print(f"Marca: {self.__marca} | Modelo: {self.__modelo} | Ano: {self.__ano} | {'Ligado' if self.__ligado else 'Desligado'}")
        
def main():
    c1 = Carro('Ford', 'Fiesta', 2020)
    c1.mostrarInfo()
    c1.ligar()
    c1.mostrarInfo()
    c1.desligar()
    c1.mostrarInfo()
main()