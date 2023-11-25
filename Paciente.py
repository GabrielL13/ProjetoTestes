import requests
import json
from Usuario import Usuario
from datetime import datetime,timezone
from Avaliacao import Avaliacao

class Paciente(Usuario):

    db = "https://projetotestes-459ea-default-rtdb.firebaseio.com"

    def __init__(self,nome, senha, cpf, telefone, rg, cartaoSus,endereco,data_de_nascimento,estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais):
        super().__init__(nome, senha, cpf, telefone, rg, cartaoSus,endereco, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
        
    def solicitar_consulta(self,user):
        data = str(datetime.now())
        dado = {"data":data,"cpf":user.get_cpf(),"nome":user.get_nome()}
        dado = json.dumps(dado)
        pedido = requests.put(f"{self.db}/Requisição/{user.cpf}.json", data=dado)
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
        
        
#   cancelar_consulta(string):void
#   obter_valor_consulta(string):float
#   realizar_pagamento(float):boolean