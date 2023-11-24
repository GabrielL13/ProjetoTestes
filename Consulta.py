from datetime import datetime

class Consulta:
    def __init__(self, id_consulta="", data_horario=None, nome_dentista="", nome_paciente="",
                 cpf_dentista="", cpf_paciente="", descricao=""):
        self.id_consulta = id_consulta
        self.data_horario = data_horario 
        self.nome_dentista = nome_dentista
        self.nome_paciente = nome_paciente
        self.cpf_dentista = cpf_dentista
        self.cpf_paciente = cpf_paciente
        self.descricao = descricao

    def get_id_consulta(self):
        return self.id_consulta

    def set_id_consulta(self, id_consulta):
        self.id_consulta = id_consulta

    def get_data_horario(self):
        return self.data_horario

    def set_data_horario(self, data_horario):
        self.data_horario = data_horario

    def get_nome_dentista(self):
        return self.nome_dentista

    def set_nome_dentista(self, nome_dentista):
        self.nome_dentista = nome_dentista

    def get_nome_paciente(self):
        return self.nome_paciente

    def set_nome_paciente(self, nome_paciente):
        self.nome_paciente = nome_paciente

    def get_cpf_dentista(self):
        return self.cpf_dentista

    def set_cpf_dentista(self, cpf_dentista):
        self.cpf_dentista = cpf_dentista

    def get_cpf_paciente(self):
        return self.cpf_paciente

    def set_cpf_paciente(self, cpf_paciente):
        self.cpf_paciente = cpf_paciente

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao
