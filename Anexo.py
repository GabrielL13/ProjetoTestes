class Anexo:
    def __init__(self, id_anexo="", tipo_de_anexo="", nome_paciente="", cpf_paciente="",
                 info="", info_adicionais="", cro_dentista=""):
        self.id_anexo = id_anexo
        self.tipo_de_anexo = tipo_de_anexo
        self.nome_paciente = nome_paciente
        self.cpf_paciente = cpf_paciente
        self.info = info
        self.info_adicionais = info_adicionais
        self.cro_dentista = cro_dentista

    def get_id_anexo(self):
        return self.id_anexo

    def set_id_anexo(self, id_anexo):
        self.id_anexo = id_anexo

    def get_tipo_de_anexo(self):
        return self.tipo_de_anexo

    def set_tipo_de_anexo(self, tipo_de_anexo):
        self.tipo_de_anexo = tipo_de_anexo

    def get_nome_paciente(self):
        return self.nome_paciente

    def set_nome_paciente(self, nome_paciente):
        self.nome_paciente = nome_paciente

    def get_cpf_paciente(self):
        return self.cpf_paciente

    def set_cpf_paciente(self, cpf_paciente):
        self.cpf_paciente = cpf_paciente

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def get_info_adicionais(self):
        return self.info_adicionais

    def set_info_adicionais(self, info_adicionais):
        self.info_adicionais = info_adicionais

    def get_cro_dentista(self):
        return self.cro_dentista

    def set_cro_dentista(self, cro_dentista):
        self.cro_dentista = cro_dentista
