class Produto:
    def __init__(self, nome: str, preco: float, qtd_estoque: int) -> None:
        self.nome = nome
        self.preco = preco
        self.qtd_estoque = qtd_estoque

    def comprar(self, qtd: int) -> None:
        if self.qtd_estoque < qtd:
            print('Não foi possível comprar!')
        else:
            self.qtd_estoque -= qtd
            print('Produto comprado com sucesso!')

    def reporEstoque(self, qtd: int) -> None:
        self.qtd_estoque += qtd
        print('Produto reposto com sucesso!')

    def mostrar_info(self) -> None:
        return f'{self.nome} | Preço: {self.preco} | Qtd: {self.qtd_estoque}'
    

class Loja:
    def __init__(self) -> None:
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def mostrar_produtos(self):
        if self.produtos == []:
            print('Nenhum produto cadastrado!')
        else:
            print('-' * 40)
            for indice, produto in enumerate(self.produtos, start=1):
                print(f'{indice}- {produto.mostrar_info()}')
            print('-' * 40)

def main():
    p1 = Produto('Detergente', 3.50, 15)
    p2 = Produto('Sabonete', 3.90, 10)

    loja = Loja()
    loja.adicionar_produto(p1)
    loja.adicionar_produto(p2)

    p1.comprar(4)
    p2.comprar(8)
    loja.mostrar_produtos()
    p1.reporEstoque(5)
    loja.mostrar_produtos()
    p1.comprar(6)
    loja.mostrar_produtos()
    p2.comprar(3)
    p2.reporEstoque(8)
    loja.mostrar_produtos()
main()