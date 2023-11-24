from datetime import datetime

class Mensagem:
    def __init__(self, id_mensagem="", cpf_emissor="", cpf_receptor="", texto=""):
        self.id_mensagem = id_mensagem
        self.cpf_emissor = cpf_emissor
        self.cpf_receptor = cpf_receptor
        self.texto = texto
        self.data = datetime.now()

    def get_id_mensagem(self):
        return self.id_mensagem

    def set_id_mensagem(self, id_mensagem):
        self.id_mensagem = id_mensagem

    def get_cpf_emissor(self):
        return self.cpf_emissor

    def set_cpf_emissor(self, cpf_emissor):
        self.cpf_emissor = cpf_emissor

    def get_cpf_receptor(self):
        return self.cpf_receptor

    def set_cpf_receptor(self, cpf_receptor):
        self.cpf_receptor = cpf_receptor

    def get_texto(self):
        return self.texto

    def set_texto(self, texto):
        self.texto = texto

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
