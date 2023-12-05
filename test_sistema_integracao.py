import pytest
from Sistema import Sistema
from datetime import datetime
from Admin import Admin
from Dentista import Dentista 
from Paciente import Paciente

class TestSistema():

    sistema = Sistema()
    sistema.login = True
    
    # CNT1 - Cadastro de Paciente
    @pytest.mark.run(order=1)
    def test_cadastro_paciente(self):
        self.sistema.user = Admin()

        # CT1 - Cadastro de um novo paciente com informações válidas
        assert self.sistema.criar_ficha(nome="Teste1", cpf="teste", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        
        # CT2 - Tentativa de cadastro de um paciente com CPF já existente
        assert not self.sistema.criar_ficha(nome="Teste2", cpf="teste", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")
        
        # CT3 - Tentativa de cadastro de um paciente sem preencher algum campo
        assert not self.sistema.criar_ficha(nome="Teste3", cpf="-99999999", senha="teste123",
                                                rg="1234567", cartaoSus="sus123", rua="ruateste",
                                                bairro="bairroteste", cidade="cidadeteste", numero="1", cep="cep123",
                                                referencia="semref", data_de_nascimento=datetime.now(),
                                                estado_civil="estado", tipo_sanguineo="O+", nacionalidade="paisteste",
                                                sexo="sexoteste0", info_adicionais="add")
        
        # CT4 - Atualizar cadastro de paciente existente
        assert self.sistema.atualizar_cadastro(nome="TesteAtualiza1", cpf="teste", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")

        # CT5 - Atualizar cadastro de paciente inexistente
        assert not self.sistema.atualizar_cadastro(nome="TesteAtualiza2", cpf="0909091029103", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        
        # CT6 - Tentativa de cadastro sem estar logado
        self.sistema.login = False
        assert not self.sistema.criar_ficha(nome="Teste6", cpf="teste6", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")

        # CT7 - Tentativa de cadastro sem ser Atendente
        self.sistema.login = True
        self.sistema.user = Dentista()
        assert not self.sistema.criar_ficha(nome="Teste7", cpf="teste7", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")
        self.sistema.user = Paciente()
        assert not self.sistema.criar_ficha(nome="Teste8", cpf="teste8", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")

    
    # CNT2 - Cadastro de Dentista
    @pytest.mark.run(order=2)
    def test_cadastro_dentista(self):
        self.sistema.user = Admin()

        # CT1 - Cadastro de um novo paciente com informações válidas
        assert self.sistema.criar_ficha_dentista(crm="crmteste",estado="estado",nome="Teste1", cpf="teste", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        
        # CT2 - Tentativa de cadastro de um paciente com CPF já existente
        assert not self.sistema.criar_ficha_dentista(crm="crmteste",estado="estado",nome="Teste2", cpf="teste", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")
        
        # CT3 - Tentativa de cadastro de um paciente sem preencher algum campo
        assert not self.sistema.criar_ficha_dentista(crm="crmteste",estado="estado",nome="Teste3", cpf="-99999999", senha="teste123",
                                                rg="1234567", cartaoSus="sus123", rua="ruateste",
                                                bairro="bairroteste", cidade="cidadeteste", numero="1", cep="cep123",
                                                referencia="semref", data_de_nascimento=datetime.now(),
                                                estado_civil="estado", tipo_sanguineo="O+", nacionalidade="paisteste",
                                                sexo="sexoteste0", info_adicionais="add")
        
        # CT4 - Tentativa de cadastro sem estar logado
        self.sistema.login = False
        assert not self.sistema.criar_ficha_dentista(crm="crmteste",estado="estado",nome="Teste4", cpf="teste4", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")

        # CT5 - Tentativa de cadastro sem ser Atendente
        self.sistema.login = True
        self.sistema.user = Dentista()
        assert not self.sistema.criar_ficha_dentista(crm="crmteste",estado="estado",nome="Teste5", cpf="teste5", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")
        self.sistema.user = Paciente()
        assert not self.sistema.criar_ficha_dentista(crm="crmteste",estado="estado",nome="Teste5", cpf="teste5", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")
   

   # CNT3 - Cadastro de Atendente
    @pytest.mark.run(order=3)
    def test_cadastro_atendente(self):
        self.sistema.user = Admin()

        # CT1 - Cadastro de um novo paciente com informações válidas
        assert self.sistema.criar_ficha_atendente(nome="Teste1", cpf="teste", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        
        # CT2 - Tentativa de cadastro de um paciente com CPF já existente
        assert not self.sistema.criar_ficha_atendente(nome="Teste2", cpf="teste", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")
        
        # CT3 - Tentativa de cadastro de um paciente sem preencher algum campo
        assert not self.sistema.criar_ficha_atendente(nome="Teste3", cpf="-99999999", senha="teste123",
                                                rg="1234567", cartaoSus="sus123", rua="ruateste",
                                                bairro="bairroteste", cidade="cidadeteste", numero="1", cep="cep123",
                                                referencia="semref", data_de_nascimento=datetime.now(),
                                                estado_civil="estado", tipo_sanguineo="O+", nacionalidade="paisteste",
                                                sexo="sexoteste0", info_adicionais="add")
       
        # CT4 - Tentativa de cadastro sem estar logado
        self.sistema.login = False
        assert not self.sistema.criar_ficha_atendente(nome="Teste5", cpf="teste5", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        
        # CT5 - Tentativa de cadastro sem ser Atendente
        self.sistema.login = True
        self.sistema.user = Dentista()
        assert not self.sistema.criar_ficha_atendente(nome="Teste6", cpf="teste6", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        self.sistema.user = Paciente()
        assert not self.sistema.criar_ficha_atendente(nome="Teste7", cpf="teste7", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        
    """
    # CNT4 - Solicitar Agendamento de Consultas
    @pytest.mark.run(order=4)
    def test_solicitacao_consulta(self):
        
        # CT1 - Visualizar solicitações sem elas existirem
        assert not self.admin.ver_solicitacoes()

        # CT2 - Solicitação do Paciente de uma Consulta
        assert self.paciente.solicitar_consulta()

        # CT3 - Visualizar solicitações com sucesso
        assert self.admin.ver_solicitacoes()

    
    # CNT5 - Agendamento de Consultas
    @pytest.mark.run(order=5)
    def test_manipular_consulta(self):

        # CT1 - Marcar uma consulta com solicitação pré-cadastrada
        self.admin.criar_ficha(nome="TesteConsulta", cpf="admin", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        assert self.admin.agendar_consulta(cpf="admin",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="consulta_teste1")
        
        # CT2 - Tentativa de marcar consulta sem cadastro
        assert not self.admin.agendar_consulta(cpf="9431031",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="consulta_teste1")
        
        # CT3 - Tentativa de marcar consulta que já existe (reagendamento)
        assert self.admin.agendar_consulta(cpf="admin",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="reagentamento")
        
        # CT4 - Tentativa de marcar consulta sem solicitação prévia
        assert self.admin.agendar_consulta(cpf="teste",data=datetime.now()
                                    ,nome_dentista="teste",cpf_dentista="teste",descricao="reagentamento")
        
        # CT5 - Cancelar consulta existente
        assert self.admin.cancelar_consulta_admin(cpf="teste",cpf_dentista="teste")
        assert self.dentista.cancelar_consulta(cpf="admin")

        # CT6 - Cancelar consulta inexistente de um dentista inexistente
        assert not self.admin.cancelar_consulta_admin(cpf="-10390193",cpf_dentista="admin")

        # CT7 - Cancelar consulta inexistente de um dentista paciente
        assert not self.admin.cancelar_consulta_admin(cpf="teste",cpf_dentista="-090909")


    # CNT6 - Verificar avaliação de atendimento
    @pytest.mark.run(order=6)
    def test_verificar_avaliacoes(self):

        # CT1 - Fazer Avaliação com sucesso
        assert self.paciente.avaliar_atendimento(nota=5,texto="avaliação teste 1")
        assert self.paciente.avaliar_atendimento(nota=4.5,texto="avaliação teste 2")
        assert self.paciente.avaliar_atendimento(nota="5",texto="avaliação teste 3")

        # CT2 - Visualizar avaliações registradas 
        assert not isinstance(self.admin.verificar_avaliacoes(),bool)

        # CT3 - Deletar as avaliações com sucesso
        assert self.admin.deletar_avaliacoes()

        # CT4 - Deletar as avaliações sem existirem
        assert not self.admin.deletar_avaliacoes()

        # CT5 - Verificar avaliações sem ter recebido nenhuma
        assert not self.admin.verificar_avaliacoes()

    
    # CNT7 - Visualizar informações de paciente
    @pytest.mark.run(order=9) 
    def test_visualizar_informacoes_paciente(self):

        # CT1 - Visualizar informações de um paciente existente
        assert self.dentista.ver_historico_paciente(cpf="admin")
        assert self.admin.ver_historico_paciente(cpf="admin")
        assert self.paciente.ver_registros()

        # CT2 - Tentativa de visualizar paciente inexistente
        assert not self.dentista.ver_historico_paciente(cpf="0129102")
        assert not self.admin.ver_historico_paciente(cpf="af3f3f3")

        # CT3 - Tentativa de visualizar paciente sem historico
        pacienteteste = Paciente(cpf="teste")
        assert not self.dentista.ver_historico_paciente(cpf="teste")
        assert not self.admin.ver_historico_paciente(cpf="teste")
        assert not pacienteteste.ver_registros()

    
    # CNT8 - Realização de Pagamento
    @pytest.mark.run(order=7)
    def test_realizar_pagamento(self):

        # CT1 - Anexar pagamento com sucesso
        assert self.admin.anexa_pagamento(cpf="admin",valor=50.75,moeda="real")
        assert self.admin.anexa_pagamento(cpf="teste",valor="10",moeda="euro")

        # CT2 - Tentativa de anexar pagamento para paciente inexistente
        assert not self.admin.anexa_pagamento(cpf="-920313b",valor = 50,moeda = "dolar")

        # CT3 - Tentativa de realizar pagamento sem ter valor suficiente
        assert not self.paciente.realizar_pagamento(pagamento=50.1,tipo_pagamento="cartao de debito")
        assert not self.paciente.realizar_pagamento(pagamento="50",tipo_pagamento="cartao de credito")
        assert not self.paciente.realizar_pagamento(pagamento=50,tipo_pagamento="dinheiro")

        # CT4 - Tentativa de realizar pagamento sem selecionar tipo de pagamento
        assert not self.paciente.realizar_pagamento(pagamento=60)

        # CT5 - Realizar pagamento com sucesso
        assert self.paciente.realizar_pagamento(pagamento=51,tipo_pagamento="dinheiro")

        # CT6 - Realizar pagamento que não existe 
        assert not self.paciente.realizar_pagamento(pagamento=51,tipo_pagamento="fiado")


    # CNT9 - Manipulação Histórico paciente
    @pytest.mark.run(order=8)
    def test_adicionar_historico_paciente(self):

        # CT1 - Adicionar anexo ao paciente com sucesso
        assert self.dentista.adicionar_anexo(cpf="admin",tipo="receita",info="remedio antibiótico",infoadd="12 em 12 horas")

        # CT2 - Adicionar anexo ao paciente inexistente
        assert not self.dentista.adicionar_anexo(cpf="-193932r",tipo="atestado",info="cirurgia odontológica",infoadd="15 dias de repouso")

        # CT3 - Arquivar consulta existente
        self.admin.agendar_consulta(cpf="admin",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="reagentamento")
        assert self.dentista.arquivar_consulta(cpf="admin")

        # CT4 - Arquivar consulta inexistente
        assert not self.dentista.arquivar_consulta(cpf="admin")

    
    # CNT10 - Visualizar informações de dentista
    @pytest.mark.run(order=10) 
    def test_visualizar_informacoes_dentista(self):
    
        # CT1 - Visualizar informações dos dentistas cadastrados
        assert not isinstance(self.admin.visualizar_dentistas(),bool)

        # CT2 - Visualizar informações de um dentista existente
        assert not isinstance(self.admin.visualizar_dentista(cpf="teste"),bool)

        # CT3 - Tentativa de visualizar dentista inexistente
        assert isinstance(self.admin.visualizar_dentista(cpf="-1291839j"),bool)

        # CT4 - Tentativa de visualizar agenda de dentista existente
        self.admin.agendar_consulta(cpf="admin",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="reagentamento")
        self.admin.agendar_consulta(cpf="teste",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="reagentamento")
        assert not isinstance(self.admin.ver_agenda_dentista(cpf="admin"),bool)
        assert not isinstance(self.dentista.ver_agenda(),bool)
        assert (self.dentista.ver_agenda() == self.admin.ver_agenda_dentista(cpf="admin"))

        # CT5 - Tentativa de visualizar agenda de dentista existente mas sem consultas registradas
        self.dentista.cancelar_consulta(cpf="admin")
        self.dentista.cancelar_consulta(cpf="teste")
        dentista = Dentista(cpf="teste")
        assert  isinstance(self.admin.ver_agenda_dentista(cpf="teste"),bool)
        assert  isinstance(dentista.ver_agenda(),bool)
    """