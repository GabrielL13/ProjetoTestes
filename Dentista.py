from Usuario import Usuario

class Dentista(Usuario):

    def __init__(self,crm,estado,nome,senha,cpf,telefone,rg,cartaoSus,endereco,data_de_nascimento,estado_civil,tipo_sanguineo,nacionalidade,sexo,info_adicionais,):
        super().__init__(nome,senha,cpf,telefone,rg,cartaoSus,endereco,data_de_nascimento,estado_civil,tipo_sanguineo,nacionalidade,sexo,info_adicionais)
        self.crm = crm
        self.estado = estado
        
#   buscar_historico(string):list
#   buscar_dados(string):Paciente
#   buscar_atividade():list
#   confirmar_consulta():boolean
#   adicionar_anexo(Anexo):boolean
#   notificar_paciente(Mensagem):boolean
#   ver_agenda():Agenda
#   solicitar_reagenda():void