class Funcionario():
    bonus = 10 # porcento
    def __init__(self, nome: str, id: int, salario: float) -> None:
        self.nome = nome
        self.id = id
        self.salario = salario
        self.bonificacao = 0

    def mostrar_detalhes(self) -> str:
        return f'{type(self).__name__}: {self.nome} | Id: {self.id} | Salário: R$ {self.salario:.2f}'
    
    def calcular_bonificacao(self) -> str:
        self.bonificacao = self.salario * (self.bonus/100)
        return f'Bonificação do(a) {self.nome}: R$ {self.salario + self.bonificacao:.2f} (+ R$ {self.bonificacao:.2f})'
        
class Gerente(Funcionario):
    bonus = 100 # reais
    def __init__(self, nome: str, id: int, salario: float) -> None:
        super().__init__(nome, id, salario)
        self.equipe = []

    def adicionar_funcionario_equipe(self, func: Funcionario) -> None:
        self.equipe.append(func)
        print(f'Funcionário(a) {func.nome} adicionado com sucesso à equipe do(a) {self.nome}!')

    def remover_funcionario(self, func: Funcionario) -> None:
        if func in self.equipe:
            self.equipe.remove(func)
            print(f'Funcionário(a) {func.nome} removido(a) com sucesso!')
        else:
            print(f'O(A) funcionário(a) {func.nome} não está na equipe!')

    def calcular_bonificacao(self) -> str:
        self.bonificacao = len(self.equipe) * self.bonus
        return f'Bonificação do(a) {self.nome}: R$ {self.salario + self.bonificacao:.2f} (+ R$ {self.bonificacao:.2f})'

class Engenheiro(Funcionario):
    bonus = 20 # porcento
    def __init__(self, nome: str, id: int, salario: float, setor: str) -> None:
        super().__init__(nome, id, salario)
        self.setor = setor

    def detalhes_setor(self) -> str:
        match self.setor.lower():
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
        return f'Bonificação do(a) {self.nome}: R$ {self.salario + self.bonificacao:.2f} (+ R$ {self.bonificacao:.2f})'

class Departamento:
    lista = []
    def __init__(self) -> None:
        self.funcionarios = []
        self.gerentes = []
        self.engenheiros = []
        self.total = 0
        self.bonificacao = 0
        Departamento.lista.append(self)

    def adicionar_funcionarios(self, funcionarios: list):
        for funcionario in funcionarios:
            self.funcionarios.append(funcionario)

    def adicionar_gerentes(self, gerentes: list):
        for gerente in gerentes:
            self.gerentes.append(gerente)

    def adicionar_engenheiros(self, engenheiros: list):
        for engenheiro in engenheiros:
            self.engenheiros.append(engenheiro)

    def calcular_salario_total(self) -> str:
        for item in self.funcionarios + self.gerentes + self.engenheiros: # junção das 2 listas
            self.total += item.salario
        return f'Salário total: R$ {self.total:.2f}'
    
    def calcular_total_bonificacao(self) -> str:
        for item in self.funcionarios + self.gerentes + self.engenheiros: # junção das 2 listas
            self.bonificacao += item.bonificacao
        return f'Bonificação total: R$ {self.bonificacao:.2f}\nBonificação com salário: R$ {self.total + self.bonificacao:.2f}'

def calcular_receita_total() -> str:
    soma_salario = 0
    soma_bonificacao = 0
    for departamento in Departamento.lista:
        soma_salario += departamento.total
        soma_bonificacao += departamento.bonificacao
    return f'Receita total: R$ {soma_salario:.2f}\n' + \
           f'Receita com bonificação: R$ {soma_salario + soma_bonificacao:.2f} (+ R$ {soma_bonificacao:.2f})'

def main():
    ti = Departamento()
    rh = Departamento()

    e1 = Engenheiro('João', 3847, 3000.00, 'Desenvolvimento')
    e2 = Engenheiro('Maria', 5870, 3100.00, 'Infraestrutura')
    e3 = Engenheiro('José', 2763, 2500.0, 'Testes')
    e4 = Engenheiro('Daniel', 5678, 3500.00, 'Suporte')

    f1 = Funcionario('Gabriel', 2938, 2000.00)
    f2 = Funcionario('Henrique', 9374, 2100.00)
    f3 = Funcionario('Lívia', 3495, 2200.00)

    g1 = Gerente('Rodrigo', 1234, 4500.00)
    g2 = Gerente('Leandro', 3857, 4200.00)

    ti.adicionar_engenheiros([e1, e2, e3])
    ti.adicionar_gerentes([g1])

    rh.adicionar_funcionarios([f1, f2, f3])
    rh.adicionar_gerentes([g2])

    print('-' * 70)
    print(g1.mostrar_detalhes())
    print('-' * 70)
    g1.adicionar_funcionario_equipe(e1)
    g1.adicionar_funcionario_equipe(e2)
    g1.adicionar_funcionario_equipe(e3)
    g1.calcular_bonificacao()
    print('-' * 70)

    print(g2.mostrar_detalhes())
    print('-' * 70)
    g2.adicionar_funcionario_equipe(f1)
    g2.adicionar_funcionario_equipe(f2)
    g2.adicionar_funcionario_equipe(f3)
    g2.calcular_bonificacao()
    print('-' * 70)

    print(e1.mostrar_detalhes())
    print('-' * 70)
    print(e1.calcular_bonificacao())
    print(e2.calcular_bonificacao())
    print(e3.calcular_bonificacao())
    print('-' * 70)

    print(f3.mostrar_detalhes())
    print('-' * 70)
    print(f1.calcular_bonificacao())
    print(f2.calcular_bonificacao())
    print(f3.calcular_bonificacao())
    print('-' * 70)

    g1.remover_funcionario(e1)
    g1.remover_funcionario(e4)
    print('-' * 70)

    print(f'Suporte Técnico: {e4.detalhes_setor()}')

    print('-' * 70)

    print('Departamento de TI:')
    print('-' * 70)
    print(ti.calcular_salario_total())
    print(ti.calcular_total_bonificacao())
    print('-' * 70)

    print('Departamento de RH:')
    print('-' * 70)
    print(rh.calcular_salario_total())
    print(rh.calcular_total_bonificacao())
    print('-' * 70)

    print(calcular_receita_total())
    print('-' * 70)
main()