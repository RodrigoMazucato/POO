from abc import ABC, abstractmethod
class Funcionario(ABC):
    bonus = 10 # porcento
    def __init__(self, nome: str, id: int, salario: float) -> None:
        self.nome = nome
        self.id = id
        self.salario = salario
        self.bonificacao = 0

    def mostrar_detalhes(self) -> str:
        return f'{type(self).__name__}: {self.nome} | Id: {self.id} | Salário: R$ {self.salario:.2f}'

    @abstractmethod
    def calcular_bonificacao(self) -> str:
        pass
        
class Gerente(Funcionario):
    bonus = 100 # reais
    def __init__(self, nome: str, id: int, salario: float) -> None:
        super().__init__(nome, id, salario)
        self.equipe = []
        Departamento.gerentes.append(self)

    def adicionar_funcionario(self, func: Funcionario) -> None:
        self.equipe.append(func)
        print(f'Funcionário(a) {func.nome} adicionado com sucesso!')

    def remover_funcionario(self, func: Funcionario) -> None:
        if func in self.equipe:
            self.equipe.remove(func)
            print(f'Funcionário(a) {func.nome} removido(a) com sucesso!')
        else:
            print(f'O(A) funcionário(a) {func.nome} não está na equipe!')

    def calcular_bonificacao(self) -> str:
        self.bonificacao = len(self.equipe) * self.bonus
        return f'Bonificação: R$ {self.salario + self.bonificacao:.2f} (+ R$ {self.bonificacao:.2f})'

class Engenheiro(Funcionario):
    bonus = 20 # porcento
    def __init__(self, nome: str, id: int, salario: float, departamento: str) -> None:
        super().__init__(nome, id, salario)
        self.departamento = departamento
        Departamento.engenheiros.append(self)

    def detalhes_departamento(self) -> str:
        match self.departamento.lower():
            case 'suporte' | 'suporte técnico':
                return 'Lida com as consultas e problemas dos usuários finais, oferecendo suporte técnico e resolvendo questões operacionais.'
            
            case 'rh' | 'recursos humanos':
                return 'Gerencia as necessidades específicas de recursos humanos para a área de TI, incluindo recrutamento, treinamento e retenção de talentos.'
            
            case 'infraestrutura' | 'infra':
                return 'Gerencia a infraestrutura de TI, incluindo servidores, redes, armazenamento e operações diárias para garantir o bom funcionamento dos sistemas.'
            
            case 'desenvolvimento':
                return 'A equipe de desenvolvimento de software é responsável por escrever código, criar aplicativos e sistemas de software.'
            
            case 'testes' | 'qualidade' | 'qa':
                return 'Garante a qualidade do software por meio de testes, controle de qualidade e implementação de práticas de desenvolvimento de software.'
            
            case _:
                return 'Departamento não cadastrado!'

    def calcular_bonificacao(self) -> str:
        self.bonificacao = self.salario * (self.bonus/100)
        return f'Bonificação: R$ {self.salario + self.bonificacao:.2f} (+ R$ {self.bonificacao:.2f})'

class Departamento:
    gerentes = []
    engenheiros = []
    total = 0
    bonificacao = 0

    def calcular_salario_total(self) -> str:
        
        for item in self.gerentes:
            self.total += item.salario

        for item in self.engenheiros:
            self.total += item.salario

        return f'Salário total: R$ {self.total:.2f}'
    
    def calcular_total_bonificacao(self) -> str:
        for item in self.gerentes:
            self.bonificacao += item.bonificacao

        for item in self.engenheiros:
            self.bonificacao += item.bonificacao

        return f'Bonificação total: R$ {self.bonificacao:.2f}\nBonificação com salário: R$ {self.total + self.bonificacao:.2f}'


def main():
    dep = Departamento()
    e1 = Engenheiro('João', 3847, 3000.00, 'Testes')
    e2 = Engenheiro('Maria', 5870, 3100.00, 'Infraestrutura')
    e3 = Engenheiro('José', 2763, 2500.0, 'Suporte')
    e4 = Engenheiro('Daniel', 5678, 3500.00, 'Desenvolvimento')
    g1 = Gerente('Rodrigo', 1234, 4500.00)

    print(g1.mostrar_detalhes())
    g1.adicionar_funcionario(e1)
    g1.adicionar_funcionario(e2)
    g1.adicionar_funcionario(e3)

    print(e1.mostrar_detalhes())
    print(e1.calcular_bonificacao())
    print(e2.mostrar_detalhes())
    print(e2.calcular_bonificacao())
    print(e3.mostrar_detalhes())
    print(e3.calcular_bonificacao())

    g1.remover_funcionario(e1)
    g1.remover_funcionario(e4)

    print(e4.detalhes_departamento())

    print(dep.calcular_salario_total())
    print(dep.calcular_total_bonificacao())

main()