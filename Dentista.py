import requests
import json
from Usuario import Usuario
from Anexo import Anexo
from collections import OrderedDict
from datetime import datetime

class Dentista(Usuario):

    db = "https://projetotestes-459ea-default-rtdb.firebaseio.com"

    def __init__(self,crm="",estado="",nome="DentistaAdmin",senha="",cpf="admin",telefone="",rg="",cartaoSus="",endereco="",data_de_nascimento="",estado_civil="",tipo_sanguineo="",nacionalidade="",sexo="",info_adicionais=""):
        super().__init__(nome,senha,cpf,telefone,rg,cartaoSus,endereco,data_de_nascimento,estado_civil,tipo_sanguineo,nacionalidade,sexo,info_adicionais)
        self.crm = crm
        self.estado = estado

    def ver_agenda(self):
        busca = requests.get(f"{self.db}/Consulta/{self.get_cpf()}.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                d_ordenado = sorted(busca.items(), key=lambda item: item[1]["data_horario"])
                dicionario_ordenado = OrderedDict(d_ordenado)
                return dict(dicionario_ordenado) 
            else:
                print("Agenda Não Existe")
                return False
        else:
            print("Erro na Busca")
            return False
        
    def adicionar_anexo(self,cpf,tipo,info,infoadd):
        data = str(datetime.now())
        anexo = Anexo(tipo,data,cpf,info,infoadd)
        anexo = anexo.__dict__
        anexo = json.dumps(anexo)
        response = requests.post(f"{self.db}/Historico/{cpf}/Anexos.json", data=anexo)
        if response.ok:
            return True
        else:
            print("Erro ao criar Anexo. Código de status:", response.status_code)
            return False

    def cancelar_consulta(self, cpf):
        try:
            url = f"{self.db}/Consulta/{self.get_cpf()}/{cpf}.json"
            busca = requests.get(url)
            if busca.ok:
                busca = busca.json()
                if (busca is None):
                        print(f"Erro ao procurar consulta.")
                        return False
            deletar = requests.delete(url)
            if deletar.ok:
                print(f"A consulta {cpf} foi deletada com sucesso.")
                return True
            else:
                print(f"Erro ao tentar deletar a consulta {cpf}.")
                return False

        except requests.exceptions.RequestException as e:
            print(f"Erro de requisição ao tentar deletar a consulta {cpf}: {e}")
            return False
        
    def ver_historico_paciente(self,cpf):
        busca = requests.get(f"{self.db}/Historico/{cpf}.json")
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
        
    def arquivar_consulta(self,cpf):
        busca = requests.get(f"{self.db}/Consulta/{self.get_cpf()}/{cpf}.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                deletar = requests.delete(f"{self.db}/Consulta/{self.get_cpf()}/{cpf}.json")
                if deletar.ok:
                    busca = json.dumps(busca)
                    response = requests.post(f"{self.db}/Historico/{self.get_cpf()}/Consultas.json", data=busca)
                    if response.ok:
                        return True
                    else:
                        print("Erro adicionar Consulta no Histórico. Código de status:", response.status_code,response.text)
                        return False    
                else:
                    print("Erro na Consulta")
                    return False
            else:
                print("Não existe Consulta pendente.")
                return False
        else:
            print("Erro na Busca")
            return False