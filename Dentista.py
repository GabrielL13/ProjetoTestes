import requests
import json
from Usuario import Usuario
from Anexo import Anexo
from collections import OrderedDict
from datetime import datetime

class Dentista(Usuario):

    db = "https://projetotestes-459ea-default-rtdb.firebaseio.com"

    def __init__(self,crm,estado,nome,senha,cpf,telefone,rg,cartaoSus,endereco,data_de_nascimento,estado_civil,tipo_sanguineo,nacionalidade,sexo,info_adicionais,):
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
                print("Paciente não existe.")
                return False
        else:
            print("Erro na Busca")
            return False
        
    def adicionar_anexo(self,cpf,tipo,info,infoadd):
        data = str(datetime.now())
        anexo = Anexo(tipo,data,cpf,info,infoadd)
        anexo = anexo.__dict__
        anexo = json.dumps(anexo)
        response = requests.post(f"{self.db}/Historico/{cpf}/Anexos/{data}.json", data=anexo)
        if response.ok:
            return True
        else:
            print("Erro ao criar Anexo. Código de status:", response.status_code)
            return False

    def cancelar_consulta(self,cpf):
        try:
            deletar = requests.delete(f"{self.db}/Consulta/{self.get_cpf()}/{cpf}.json")
            if deletar.ok:
                return True
            else:
                return False
        except:
            print("Erro ao deletar consulta.")
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

#    def buscar_historico(string):list
#    def arquivar_consulta(self):