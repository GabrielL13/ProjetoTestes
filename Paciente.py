import requests
import json
from Usuario import Usuario
from datetime import datetime,timezone

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

#   avaliar_atendimento(string) : void
#   cancelar_consulta(string):void
#   obter_valor_consulta(string):float
#   realizar_pagamento(float):boolean 
#   ver_mensagens():list
#   ver_mensagem(string):Mensagem
#   realizar_avaliação(Avaliacao):bool