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
        if self.login:
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
        else:
            print("Ação não é permitida.")
            return False
        
    def deletar_notificacoes(self):
        if self.login:
            busca = requests.get(f"{self.db}/Mensagens/{self.user.get_cpf()}.json")
            if busca.ok:
                busca = busca.json()
                if (busca is not None):
                    busca = requests.delete(f"{self.db}/Mensagens/{self.user.get_cpf()}.json")
                    if busca.ok :
                        return True
                    else:
                        print("Erro ao apagar Notificações.")
                        return(True)   
                else:
                    print("Não há Notificações.")
                    return False
            else:
                print("Erro na Busca")
                return False
        else:
            print("Ação não é permitida.")
            return False

    def fazer_logout(self):
        try:
            self.login = False
            self.user = None
            return True
        except:
            return False
        
# Ações Unicas dos Atendentes ou Administradores
        
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
            resposta = self.user.ver_solicitacoes()
            if isinstance(resposta,bool):
                return resposta
            else:
                print(resposta)
                return True
        else:
            print("Ação não é permitida.")
            return False 

    def agendar_consulta(self,data,cpf,nome_dentista,cpf_dentista,descricao):
        if self.login and isinstance(self.user,Admin) :
            if self.ver_solicitacoes():
                resposta = self.user.agendar_consulta(cpf,data,nome_dentista,cpf_dentista,descricao)
                return resposta
            else:
                print("Não Existe Requisições de Consulta.")
                return False
        else:
            print("Ação não é permitida.")
            return False 
    
    def anexa_pagamento(self,cpf,valor,moeda,data):
        if self.login and isinstance(self.user,Admin) :
            resposta = self.user.anexa_pagamento(cpf,str(valor),moeda,data)
            return resposta
        else:
            print("Ação não é permitida.")
            return False 
        
    def verificar_avaliacoes(self):
        if self.login and isinstance(self.user,Admin) :
            resposta = self.user.verificar_avaliacoes()
            if isinstance(resposta,bool):
                return resposta
            else:
                print(resposta)
                return True
        else:
            print("Ação não é permitida.")
            return False
        
    def deletar_avaliacoes(self):
        if self.login and isinstance(self.user,Admin) :
            resposta = self.user.deletar_avaliacoes()
            return resposta
        else:
            print("Ação não é permitida.")
            return False
        
    def visualizar_dentista(self,cpf):
        if self.login and isinstance(self.user,Admin) :
            resposta = self.user.visualizar_dentista(cpf)
            if isinstance(resposta,bool):
                return resposta
            else:
                print(resposta)
                return True
        else:
            print("Ação não é permitida.")
            return False
        
    def visualizar_dentistas(self):
        if self.login and isinstance(self.user,Admin) :
            resposta = self.user.visualizar_dentistas()
            if isinstance(resposta,bool):
                return resposta
            else:
                print(resposta)
                return True
        else:
            print("Ação não é permitida.")
            return False
        
    #    def atualizar_cadastro(Usuario):
            
# Dentista e Admin
         
    def visualizar_paciente(self,cpf):
        if self.login and (isinstance(self.user,Admin) or isinstance(self.user,Dentista)) :
            busca = requests.get(f"{self.db}/Paciente/{cpf}.json")
            if busca.ok:
                busca = busca.json()
                if (busca is not None):
                    print(busca)
                    return True    
                else:
                    print("Paciente não existe.")
                    return False
            else:
                print("Erro na Busca")
                return False
        else:
            print("Ação não é permitida.")
            return False
        
    def ver_historico_paciente(self,cpf):
        if self.login and (isinstance(self.user,Dentista) or isinstance(self.user,Admin)) :
            resposta = self.user.ver_historico_paciente(cpf)
            return resposta
        else:
            print("Ação não é permitida.")
            return False

# Ações Unicas dos Dentista

    def adicionar_anexo(self,cpf,tipo,info,info_adicionais):
        if self.login and isinstance(self.user,Dentista) :
            resposta = self.user.adicionar_anexo(cpf,tipo,info,info_adicionais)
            return resposta
        else:
            print("Ação não é permitida.")
            return False 

    def ver_agenda(self):
        if self.login and  isinstance(self.user,Dentista):
            resposta = self.user.ver_agenda()
            if isinstance(resposta,bool):
                return resposta
            else:
                print(resposta)
                return True
        else:
            print("Ação não é permitida.")
            return False
        
    def cancelar_consulta(self,cpf):
        if self.login and isinstance(self.user,Dentista) :
            resposta = self.user.cancelar_consulta(cpf)
            if resposta:
                self.notificar(cpf,"Consulta Cancelada, solicite um novo agendamento.")
                return resposta
            else:
                return resposta
        else:
            print("Ação não é permitida.")
            return False
        
# Ações Unicas dos Pacientes

    def solicitar_consulta(self):
        if self.login and isinstance(self.user,Paciente) :
            resposta = self.user.solicitar_consulta()
            return resposta
        else:
            print("Ação não é permitida.")
            return False 

    def avaliar_atendimento(self,nota,texto):
        if self.login and isinstance(self.user,Paciente) :
            resposta = self.user.avaliar_atendimento(nota,texto)
            return resposta
        else:
            print("Ação não é permitida.")
            return False 

    def visualizar_pagamento(self):
        if self.login and isinstance(self.user,Paciente) :
            resposta = self.user.visualizar_pagamento()
            return resposta
        else:
            print("Ação não é permitida.")
            return False 
    
    def realizar_pagamento(self,pagamento,tipo_pagamento):
        if self.login and isinstance(self.user,Paciente) :
            resposta = self.user.realizar_pagamento(pagamento,tipo_pagamento)
            return resposta
        else:
            print("Ação não é permitida.")
            return False 
        
    def ver_registros(self):
        if self.login and isinstance(self.user,Paciente) :
            resposta = self.user.ver_registros()
            return resposta
        else:
            print("Ação não é permitida.")
            return False