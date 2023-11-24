from Usuario import Usuario

class Paciente(Usuario):

    db = "https://projetotestes-459ea-default-rtdb.firebaseio.com"

    def __init__(self,nome, senha, cpf, telefone, rg, cartaoSus,endereco,data_de_nascimento,estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais):
        super().__init__(nome, senha, cpf, telefone, rg, cartaoSus,endereco, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
        

#   solicitar_consulta(): void
#   avaliar_atendimento(string) : void
#   cancelar_consulta(string):void
#   obter_valor_consulta(string):float
#   realizar_pagamento(float):boolean 
#   ver_mensagens():list
#   ver_mensagem(string):Mensagem
#   realizar_avaliação(Avaliacao):bool