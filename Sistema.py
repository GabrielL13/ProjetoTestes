import json
import requests
from Admin import Admin
from Dentista import Dentista
from Paciente import Paciente
from Mensagem import Mensagem
from datetime import datetime

class Sistema:

    db = "https://projetotestes-459ea-default-rtdb.firebaseio.com"

    def __init__(self, login=False, user=None):
        self.login = login
        self.user = user

    def fazer_login(self,tipo_usuario,cpf,senha):
        busca = requests.get(f"{self.db}/{tipo_usuario}.json")
        busca = busca.json()
        if busca is None :
            self.login = False
            print("Erro Tipo de Usuario não existe.")
            return False
        if not cpf in busca :
            self.login = False
            print("Erro CPF de Usuario não existe.")
            return False
        user = busca[cpf]
        if (user is not None):
            if user["senha"] != senha :
                print("Senha Incorreta")
                return False
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
            print("Erro ao Logar")
            return False
        else:
            self.login = False
            print("Erro no Banco de Dados")
            return False
        
    def notificar(self,cpf,mensagem):
        if self.login:
            mensagem = Mensagem(self.user.get_cpf(),cpf,mensagem)
            mensagem = mensagem.__dict__
            mensagem = json.dumps(mensagem)
            response = requests.post(f"{self.db}/Mensagens/{cpf}.json", data=mensagem)
            if response.ok:
                return True
            else:
                print("Erro ao criar requisição de Pagamento. Código de status:", response.status_code)
                return False
        else:
            print("Ação não é permitida.")
            return False
        
    def ver_notificacoes(self):
        busca = requests.get(f"{self.db}/Mensagens/{self.user.get_cpf()}.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                print(busca)
                return True    
            else:
                print("Não há Notificações.")
                return False
        else:
            print("Erro na Busca")
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

    def ver_solicitacoes(self):
        if self.login and isinstance(self.user,Admin) :
            resposta = self.user.ver_solicitacoes(self.user)
            if isinstance(resposta,bool):
                return resposta
            else:
                print(resposta)
                return True
        else:
            print("Ação não é permitida.")
            return False 

    def agendar_consulta(self,data,cpf,nome_dentista,cpf_dentista,descricao,id_consulta):
        if self.login and isinstance(self.user,Admin) :
            if self.ver_solicitacoes():
                resposta = self.user.agendar_consulta(self.user,cpf,data,nome_dentista,cpf_dentista,descricao,id_consulta)
                return resposta
            else:
                print("Não Existe Requisições de Consulta.")
                return False
        else:
            print("Ação não é permitida.")
            return False 
    
    def anexa_pagamento(self,cpf,tipo_pagamento,valor,moeda,data):
        if self.login and isinstance(self.user,Admin) :
            resposta = self.user.anexa_pagamento(cpf,tipo_pagamento,str(valor),moeda,data)
            return resposta
        else:
            print("Ação não é permitida.")
            return False 
        
#    def registrar_usuario(Usuario):boolean
#    def verificar_avaliacoes():list
#    def visualizar_dentista(string):Dentista
#    def visualizar_paciente(string):Paciente
#    def atualizar_cadastro(Usuario):

# Dentista

#   buscar_historico(string):list
#   buscar_dados(string):Paciente
#   buscar_atividade():list
#   confirmar_consulta():boolean
#   adicionar_anexo(Anexo):boolean
#   ver_agenda():Agenda

# Paciente

    def solicitar_consulta(self):
        if self.login and isinstance(self.user,Paciente) :
            resposta = self.user.solicitar_consulta(self.user)
            return resposta
        else:
            print("Ação não é permitida.")
            return False 

#   avaliar_atendimento(string) : void
#   cancelar_consulta(string):void
#   obter_valor_consulta(string):float
#   realizar_pagamento(float):boolean 
#   ver_mensagens():list
#   ver_mensagem(string):Mensagem
#   realizar_avaliação(Avaliacao):bool