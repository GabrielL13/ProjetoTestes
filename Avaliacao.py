from datetime import datetime

class Avaliacao:
    def __init__(self, texto="", nota="0"):
        self.texto = texto
        self.nota = nota
        self.data = str(datetime.now())

    def get_id_avaliacao(self):
        return self.id_avaliacao

    def set_id_avaliacao(self, id_avaliacao):
        self.id_avaliacao = id_avaliacao

    def get_texto(self):
        return self.texto

    def set_texto(self, texto):
        self.texto = texto

    def get_nota(self):
        return self.nota

    def set_nota(self, nota):
        self.nota = nota

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
