class Funcionario:
    def __init__(self, nome: str, id: int, salario: float) -> None:
        self.nome = nome
        self.id = id
        self.salario = salario

    def mostrar_detalhes(self):
        pass

    def calcular_bonificacao(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome: str, id: int, salario: float) -> None:
        super().__init__(nome, id, salario)
        self.equipe = []
    
    def adicionar_funcionario(self):
        pass

    def remover_funcionario(self):
        pass

class Engenheiro(Funcionario):
    def __init__(self, nome: str, id: int, salario: float, departamento: str) -> None:
        super().__init__(nome, id, salario)
        self.departamento = departamento

    def 