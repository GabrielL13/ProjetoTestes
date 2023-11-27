class Usuario:
    def __init__(self,nome="", senha="", cpf="", telefone="", rg="", cartaoSus="",endereco=None, data_de_nascimento="", estado_civil="", tipo_sanguineo="", nacionalidade="", sexo="", info_adicionais=""):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.telefone = telefone
        self.rg = rg
        self.cartaoSus = cartaoSus
        self.endereco = endereco
        self.data_de_nascimento = data_de_nascimento
        self.estado_civil = estado_civil
        self.tipo_sanguineo = tipo_sanguineo
        self.nacionalidade = nacionalidade
        self.sexo = sexo
        self.info_adicionais = info_adicionais

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_senha(self):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_rg(self):
        return self.rg

    def set_rg(self, rg):
        self.rg = rg

    def get_cartao_sus(self):
        return self.cartaoSus

    def set_cartao_sus(self, cartao_sus):
        self.cartaoSus = cartao_sus

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_data_de_nascimento(self):
        return self.data_de_nascimento

    def set_data_de_nascimento(self, data_de_nascimento):
        self.data_de_nascimento = data_de_nascimento

    def get_estado_civil(self):
        return self.estado_civil

    def set_estado_civil(self, estado_civil):
        self.estado_civil = estado_civil

    def get_tipo_sanguineo(self):
        return self.tipo_sanguineo

    def set_tipo_sanguineo(self, tipo_sanguineo):
        self.tipo_sanguineo = tipo_sanguineo

    def get_nacionalidade(self):
        return self.nacionalidade

    def set_nacionalidade(self, nacionalidade):
        self.nacionalidade = nacionalidade

    def get_sexo(self):
        return self.sexo

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_info_adicionais(self):
        return self.info_adicionais

    def set_info_adicionais(self, info_adicionais):
        self.info_adicionais = info_adicionais
