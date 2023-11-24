import json
import requests
from Admin import Admin
from Dentista import Dentista
from Paciente import Paciente

class Sistema:
    def __init__(self, login=False, user=None):
        self.login = login
        self.user = user
        self.db = "https://projetotestes-459ea-default-rtdb.firebaseio.com"

    def fazer_login(self,tipo_usuario,cpf,senha):
        busca = requests.get(f"{self.db}/{tipo_usuario}.json")
        busca = user.json()
        user = busca[cpf]
        if (user is not None):
            if (tipo_usuario=="Admin"):
                self.login = True
                self.user = Admin(**user)
                return True
            if (tipo_usuario=="Dentista"):
                self.login = True
                self.user = Dentista(**user)
                return True
            if (tipo_usuario=="Paciente"):
                self.login = True
                self.user = Paciente(**user)
                return True
            return False
            print("Erro ao Logar")
        else:
            self.login = False
            print("Erro ao Logar")
            return False

    def fazer_logout(self):
        try:
            self.login = False
            self.user = None
            return True
        except:
            return False
        
    def criar_ficha(self, nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais=None):
        if self.login and isinstance(self.user,Admin) :
            resposta = self.user.criar_ficha(nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
            return resposta
        else:
            print("Ação não é permitida.")
            return False

    def criar_ficha_dentista(self,crm,estado,nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais=None):
        if self.login and isinstance(self.user,Admin) :
            resposta = self.user.criar_ficha_dentista(crm,estado,nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
            return resposta
        else:
            print("Ação não é permitida.")
            return False
        
    def criar_ficha_atendente(self,nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais=None):
        if self.login and isinstance(self.user,Admin) :
            resposta = self.user.criar_ficha_atendente(nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
            return resposta
        else:
            print("Ação não é permitida.")
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

# Dentista

#   solicitar_reagenda():void
#   buscar_historico(string):list
#   buscar_dados(string):Paciente
#   buscar_atividade():list
#   confirmar_consulta():boolean
#   adicionar_anexo(Anexo):boolean
#   notificar_paciente(Mensagem):boolean
#   ver_agenda():Agenda

# Paciente

#   solicitar_consulta(): void
#   avaliar_atendimento(string) : void
#   cancelar_consulta(string):void
#   obter_valor_consulta(string):float
#   realizar_pagamento(float):boolean 
#   ver_mensagens():list
#   ver_mensagem(string):Mensagem
#   realizar_avaliação(Avaliacao):bool