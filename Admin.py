import requests
import json
from Usuario import Usuario
from Endereco import Endereco
from Paciente import Paciente
from Dentista import Dentista
from Consulta import Consulta
from datetime import datetime
from Pagamento import Pagamento

class Admin(Usuario):

    db = "https://projetotestes-459ea-default-rtdb.firebaseio.com"

    def __init__(self,nome, senha, cpf, telefone, rg, cartaoSus, endereco, data_de_nascimento,estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais):
        super().__init__(nome, senha, cpf, telefone, rg, cartaoSus,endereco, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
        

    def criar_ficha(self,nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais=None):
        busca = requests.get(f"{self.db}/Paciente.json")
        busca = busca.json()
        if (busca is not None):
            user = busca[cpf]
            if (user is not None):
                print("Ficha de Paciente já existe.")
                return False       
        endereco = Endereco(rua, bairro, cidade, cep, numero, referencia)
        usuario = Paciente(nome, senha, cpf, telefone, rg, cartaoSus,None, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
        endereco_dict = endereco.to_dict()
        usuario_dict = usuario.__dict__
        usuario_dict['endereco'] = endereco_dict
        usuario_json = json.dumps(usuario_dict)
        response = requests.put(f"{self.db}/Paciente/{cpf}.json", data=usuario_json)
        if response.ok:
            return True
        else:
            print("Erro ao criar ficha de Paciente. Código de status:", response.status_code)
            return False
            
    def criar_ficha_atendente(self, nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais):
        busca = requests.get(f"{self.db}/Admin.json")
        busca = busca.json()
        if (busca is not None):
            user = busca[cpf]
            if (user is not None):
                print("Ficha de Atendente já existe.")
                return False       
        endereco = Endereco(rua, bairro, cidade, cep, numero, referencia)
        usuario = Admin(nome, senha, cpf, telefone, rg, cartaoSus,None, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
        endereco_dict = endereco.to_dict()
        usuario_dict = usuario.__dict__
        usuario_dict['endereco'] = endereco_dict
        usuario_json = json.dumps(usuario_dict)
        response = requests.put(f"{self.db}/Admin/{cpf}.json", data=usuario_json)
        if response.ok:
            return True
        else:
            print("Erro ao criar ficha de Atendente. Código de status:", response.status_code)
            return False
        
    def criar_ficha_dentista(self,crm,estado, nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais):
        busca = requests.get(f"{self.db}/Dentista.json")
        busca = busca.json()
        if (busca is not None):
            user = busca[cpf]
            if (user is not None):
                print("Ficha de Dentista já existe.")
                return False       
        endereco = Endereco(rua, bairro, cidade, cep, numero, referencia)
        usuario = Dentista(crm,estado,nome, senha, cpf, telefone, rg, cartaoSus,None, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
        endereco_dict = endereco.to_dict()
        usuario_dict = usuario.__dict__
        usuario_dict['endereco'] = endereco_dict
        usuario_json = json.dumps(usuario_dict)
        response = requests.put(f"{self.db}/Dentista/{cpf}.json", data=usuario_json)
        if response.ok:
            return True
        else:
            print("Erro ao criar ficha de Dentista. Código de status:", response.status_code)
            return False
        
    def ver_solicitacoes(self,user):
        busca = requests.get(f"{self.db}/Requisição.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                return busca     
            else:
                return False
        else:
            print("Erro na Busca")
            return False
        
    def agendar_consulta(self,user,cpf,data,nome_dentista,cpf_dentista,descricao,id_consulta):
        busca = requests.get(f"{self.db}/Requisição.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                if cpf in busca:
                    busca = busca[cpf]
                    consulta = Consulta(id_consulta,str(data),nome_dentista,busca["nome"],cpf_dentista,busca["cpf"],descricao)
                    consulta = consulta.__dict__
                    consulta_json = json.dumps(consulta)
                    response = requests.put(f"{self.db}/Consulta/{cpf_dentista}/{id_consulta}.json", data=consulta_json)
                    if response.ok:
                        if requests.delete(f"{self.db}/Requisição/{cpf}.json").ok :
                            return True
                        else:
                            print("Falha ao retirar Requisição.")
                            return False
                    else:
                        print("Erro ao criar ficha de Consulta. Código de status:", response.status_code)
                        return False
                else:
                    print("Paciente não encontrado.")
                    return False
            else:
                print("Requisição não existe.")
                return False
        else:
            print("Erro na Busca")
            return False
        
    def anexa_pagamento(self,cpf,tipo_pagamento,valor,moeda,data):
        data = str(datetime.now()) 
        pagamento = Pagamento(data+cpf,tipo_pagamento,valor,moeda,data)
        pagamento = pagamento.__dict__
        pagamento = json.dumps(pagamento)
        response = requests.put(f"{self.db}/Pagamento/{cpf}.json", data=pagamento)
        if response.ok:
            return True
        else:
            print("Erro ao criar requisição de Pagamento. Código de status:", response.status_code)
            return False



#    def notificar(Mensagem):boolean
#    def registrar_usuario(Usuario):boolean
#    def verificar_avaliacoes():list
#    def visualizar_dentista(string):Dentista
#    def visualizar_paciente(string):Paciente
#    def atualizar_cadastro(Usuario):