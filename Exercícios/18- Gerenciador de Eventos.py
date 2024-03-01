from datetime import datetime
import locale

# Definindo o local para o português brasileiro
locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')

class Evento:
    inscritos = []
    EVENTOS = []
    def __init__(self, nome: str, local: str, data: str, capacidade: int) -> None:
        self.nome = nome
        self.local = local
        self.data = data
        self.capacidade = capacidade
        self.EVENTOS.append(self)

    def mostra_info_evento(self) -> str:
        return f'{self.nome} | Local: {self.local} | Data: {self.data} | Capacidade: {self.capacidade} pessoas'
    
    def get_eventos(self):
        print('-' * 30)
        print('EVENTOS:')
        print('-' * 30)
        for evento in self.EVENTOS:
            print(evento.mostraInfoEvento())

    def cancelar_evento(self):
        pass

    def incluir_inscrito(self, inscrito: Inscrito):
        self.inscritos.append(inscrito)

class Participante:
    ingressos_comprados = []
    def __init__(self, nome: str, email: str) -> None:
        self.__nome = nome
        self.__email = email

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def email(self) -> str:
        return self.__email

    def mostrar_ingressos(self):
        for ingresso in self.ingressos_comprados:
            print()


class Ingresso:
    def __init__(self, participante: Participante, evento: Evento) -> None:
        self.participante = participante
        self.evento = evento
        self.data_compra = datetime.now()
        self.data_formatada = self.data_compra.strftime('%d de %B de %Y - %H:%M')
        self.status_ingresso = True