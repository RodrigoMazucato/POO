class Funcionario:
    bonus = 10 # porcento
    def __init__(self, nome: str, id: int, salario: float) -> None:
        self.nome = nome
        self.id = id
        self.salario = salario
        self.bonificacao = self.salario * (1 + self.bonus/100)

    def mostrar_detalhes(self) -> str:
        return f'Nome: {self.nome} | Id: {self.id} | Salário: R$ {self.salario:.2f}'

    def calcular_bonificacao(self) -> str:
        return f'Bonificação: R$ {self.bonificacao:.2f}'
        
class Gerente(Funcionario):
    bonus = 100 # reais
    def __init__(self, nome: str, id: int, salario: float) -> None:
        super().__init__(nome, id, salario)
        self.equipe = []
    
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
        bonificacao = self.salario + len(self.equipe) * self.bonus
        return f'Bonificação: R$ {bonificacao:.2f}'

class Engenheiro(Funcionario):
    bonus = 20 # porcento
    def __init__(self, nome: str, id: int, salario: float, departamento: str) -> None:
        super().__init__(nome, id, salario)
        self.departamento = departamento

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
def main():
    f1 = Funcionario('João', 3847, 3000.00)
    f2 = Funcionario('Maria', 5870, 3100.00)
    f3 = Funcionario('José', 2763, 2500.00)
    g1 = Gerente('Rodrigo', 1234, 4500.00)
    e1 = Engenheiro('Daniel', 5678, 3500.00, 'desenvolvimento')

    g1.adicionar_funcionario(f1)
    g1.adicionar_funcionario(f2)
    g1.adicionar_funcionario(e1)

    print(f1.mostrar_detalhes())
    print(f1.calcular_bonificacao())
    print(g1.mostrar_detalhes())
    print(g1.calcular_bonificacao())
    print(e1.mostrar_detalhes())
    print(e1.calcular_bonificacao())

    g1.remover_funcionario(f1)
    g1.remover_funcionario(f3)

    print(e1.detalhes_departamento())

main()