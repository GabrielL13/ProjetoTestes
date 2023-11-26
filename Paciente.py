import requests
import json
from Usuario import Usuario
from datetime import datetime,timezone
from Avaliacao import Avaliacao

class Paciente(Usuario):

    db = "https://projetotestes-459ea-default-rtdb.firebaseio.com"

    def __init__(self,nome, senha, cpf, telefone, rg, cartaoSus,endereco,data_de_nascimento,estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais):
        super().__init__(nome, senha, cpf, telefone, rg, cartaoSus,endereco, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
        
    def solicitar_consulta(self):
        data = str(datetime.now())
        dado = {"data":data,"cpf":self.get_cpf(),"nome":self.get_nome()}
        dado = json.dumps(dado)
        pedido = requests.put(f"{self.db}/Requisição/{self.get_cpf()}.json", data=dado)
        if pedido.ok:
            return True
        else:
            print("Erro ao criar Requisição. Código de status:",pedido.status_code," ",pedido.text)
            return False
    
    def avaliar_atendimento(self,nota,texto):
        avaliacao = Avaliacao(texto,nota)
        avaliacao = avaliacao.__dict__
        avaliacao = json.dumps(avaliacao)
        print(avaliacao)
        response = requests.post(f"{self.db}/Avaliacao.json", data=avaliacao)
        if response.ok:
            return True
        else:
            print("Erro ao criar Feedback. Código de status:", response.status_code,response.text)
            return False
        
    def visualizar_pagamento(self):
        busca = requests.get(f"{self.db}/Pagamento/{self.get_cpf()}.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                return busca    
            else:
                print("Não existe Pagamentos pendentes.")
                return False
        else:
            print("Erro na Busca")
            return False
        
    def realizar_pagamento(self,pagamento,tipo_pagamento):
        busca = self.visualizar_pagamento()
        if float(busca["valor"]) > float(pagamento) :
            print("Valor Insuficiente")
            return False
        else:
            deletar = requests.delete(f"{self.db}/Pagamento/{self.get_cpf()}.json")
            if deletar.ok:
                busca["status_pagamento"] == "True"
                busca.update({"tipo_pagamento":tipo_pagamento})
                busca = json.dumps(busca)
                response = requests.post(f"{self.db}/Historico/{self.get_cpf()}/Pagamentos.json", data=busca)
                if response.ok:
                    print("Pagamento realizado com sucesso.")
                    return True
                else:
                    print("Erro adicionar Pagamento no Histórico. Código de status:", response.status_code,response.text)
                    return False    
            else:
                print("Erro no Pagamento")
                return False
            
    def ver_registros(self):
        busca = requests.get(f"{self.db}/Historico/{self.get_cpf()}.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                return busca    
            else:
                print("Paciente não existe ou não possui histórico.")
                return False
        else:
            print("Erro na Busca")
            return False