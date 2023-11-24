import requests
import json
from Usuario import Usuario
from Endereco import Endereco
from Paciente import Paciente
from Dentista import Dentista



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
        response = requests.post(f"{self.db}/Paciente/{cpf}.json", data=usuario_json)
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
        response = requests.post(f"{self.db}/Admin/{cpf}.json", data=usuario_json)
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
        response = requests.post(f"{self.db}/Dentista/{cpf}.json", data=usuario_json)
        if response.ok:
            return True
        else:
            print("Erro ao criar ficha de Dentista. Código de status:", response.status_code)
            return False
        
    
#    def agendar_paciente(self):
#    def reagendar_consulta():void
#    def anexa_pagamento(Pagamento):boolean
#    def notificar(Mensagem):boolean
#    def registrar_usuario(Usuario):boolean
#    def verificar_avaliacoes():list
#    def visualizar_dentista(string):Dentista
#    def visualizar_paciente(string):Paciente
#    def atualizar_cadastro(Usuario):