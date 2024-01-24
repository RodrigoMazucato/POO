from datetime import datetime
class Aluno:
    creditos = 4
    def __init__(self, nome: str, ano_ingresso: int, curso: str, qtd_disc_aprovadas: int) -> None:
        self.nome = nome
        self.ano_ingresso = ano_ingresso
        self.curso = curso
        self.qtd_disc_aprovadas = qtd_disc_aprovadas

    def calcular_creditos(self) -> int:
        return f'Créditos do {self.nome}: {self.qtd_disc_aprovadas * self.creditos}'
    
    def calcular_tempo_permanencia(self):
        tempo = datetime.now().year - self.ano_ingresso
        return f'Tempo de permanência: {tempo} {'ano' if tempo == 1 else 'anos'}'
    
aluno1 = Aluno('Rodrigo', 2023, 'Sistemas de Informação', 10)
print(aluno1.calcular_creditos())
print(aluno1.calcular_tempo_permanencia())

aluno2 = Aluno('Gabriel', 2021, 'Análise e Desenvolvimento de Sistemas', 9)
print(aluno2.calcular_creditos())
print(aluno2.calcular_tempo_permanencia())
