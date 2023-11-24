class Endereco:
    def __init__(self, rua, bairro, cidade, cep, numero, referencia):
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.numero = numero
        self.referencia = referencia

    def get_rua(self):
        return self.rua

    def set_rua(self, rua):
        self.rua = rua

    def get_bairro(self):
        return self.bairro

    def set_bairro(self, bairro):
        self.bairro = bairro

    def get_cidade(self):
        return self.cidade

    def set_cidade(self, cidade):
        self.cidade = cidade

    def get_cep(self):
        return self.cep

    def set_cep(self, cep):
        self.cep = cep

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def get_referencia(self):
        return self.referencia

    def set_referencia(self, referencia):
        self.referencia = referencia
    
    def to_dict(self):
        return {
            'rua': self.rua,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'cep': self.cep,
            'numero': self.numero,
            'referencia': self.referencia
        }