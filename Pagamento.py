from datetime import datetime

class Pagamento:
    def __init__(self, id_pagamento="", valor=0.0, moeda="", data=None):
        self.id_pagamento = id_pagamento
        self.valor = valor
        self.moeda = moeda
        self.data = data if data else datetime.now()
        self.status_pagamento = False

    def get_id_pagamento(self):
        return self.id_pagamento

    def set_id_pagamento(self, id_pagamento):
        self.id_pagamento = id_pagamento

    def get_tipo_pagamento(self):
        return self.tipo_pagamento

    def set_tipo_pagamento(self, tipo_pagamento):
        self.tipo_pagamento = tipo_pagamento

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_moeda(self):
        return self.moeda

    def set_moeda(self, moeda):
        self.moeda = moeda

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def is_status_pagamento(self):
        return self.status_pagamento

    def efetuar_pagamento(self):
        self.status_pagamento = True
