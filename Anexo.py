class Anexo:
    def __init__(self,tipo_de_anexo="", data="", cpf_paciente="",
                 info="", info_adicionais="",):
        self.data = data
        self.tipo_de_anexo = tipo_de_anexo
        self.cpf_paciente = cpf_paciente
        self.info = info
        self.info_adicionais = info_adicionais
    
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_tipo_de_anexo(self):
        return self.tipo_de_anexo

    def set_tipo_de_anexo(self, tipo_de_anexo):
        self.tipo_de_anexo = tipo_de_anexo

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