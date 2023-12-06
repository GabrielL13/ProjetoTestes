import pytest
from Sistema import Sistema
from datetime import datetime
from Admin import Admin
from Dentista import Dentista 
from Paciente import Paciente

class TestIntegracaoSistema():

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
        

    # CNT4 - Solicitar Agendamento de Consultas
    @pytest.mark.run(order=4)
    def test_solicitacao_consulta(self):
        self.sistema.login = True
        
        # CT1 - Visualizar solicitações sem elas 
        self.sistema.user = Admin()
        assert not self.sistema.ver_solicitacoes()

        # CT2 - Solicitação do Paciente de uma Consulta
        self.sistema.user = Paciente()
        assert self.sistema.solicitar_consulta()

        # CT3 - Visualizar solicitações com sucesso
        self.sistema.user = Admin()
        assert self.sistema.ver_solicitacoes()

        # CT4 - Solicitação sem estar logado
        self.sistema.user = Paciente()
        self.sistema.login = False
        assert not self.sistema.solicitar_consulta()

        # CT5 - Solicitação sem ser Paciente
        self.sistema.user = Admin()
        self.sistema.login = True
        assert not self.sistema.solicitar_consulta()

    
    # CNT5 - Agendamento de Consultas
    @pytest.mark.run(order=5)
    def test_manipular_consulta(self):
        self.sistema.login = True
        self.sistema.user = Admin()

        # CT1 - Marcar uma consulta com solicitação pré-cadastrada
        self.sistema.criar_ficha(nome="TesteConsulta", cpf="admin", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        assert self.sistema.agendar_consulta(cpf="admin",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="consulta_teste1")
        
        # CT2 - Tentativa de marcar consulta sem cadastro
        assert not self.sistema.agendar_consulta(cpf="9431031",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="consulta_teste1")
        
        # CT3 - Tentativa de marcar consulta que já existe (reagendamento)
        assert self.sistema.agendar_consulta(cpf="admin",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="reagentamento")
        
        # CT4 - Tentativa de marcar consulta sem solicitação prévia
        assert self.sistema.agendar_consulta(cpf="teste",data=datetime.now()
                                    ,nome_dentista="teste",cpf_dentista="teste",descricao="reagentamento")
        
        # CT5 - Cancelar consulta existente
        assert self.sistema.cancelar_consulta_admin(cpf="teste",cpf_dentista="teste")
        self.sistema.user = Dentista()
        assert self.sistema.cancelar_consulta(cpf="admin")

        # CT6 - Cancelar consulta inexistente de um dentista inexistente
        self.sistema.user = Admin()
        assert not self.sistema.cancelar_consulta_admin(cpf="-10390193",cpf_dentista="admin")

        # CT7 - Cancelar consulta inexistente de um dentista paciente
        assert not self.sistema.cancelar_consulta_admin(cpf="teste",cpf_dentista="-090909")

    
    # CNT6 - Verificar avaliação de atendimento
    @pytest.mark.run(order=6)
    def test_verificar_avaliacoes(self):
        self.sistema.login = True
        self.sistema.user = Paciente()

        # CT1 - Fazer Avaliação com sucesso
        assert self.sistema.avaliar_atendimento(nota=5,texto="avaliação teste 1")
        assert self.sistema.avaliar_atendimento(nota=4.5,texto="avaliação teste 2")
        assert self.sistema.avaliar_atendimento(nota="5",texto="avaliação teste 3")

        # CT2 - Fazer Avaliação sem estar logado
        self.sistema.login = False
        assert not self.sistema.avaliar_atendimento(nota="boa",texto="avaliação teste 4")
    
        # CT3 - Visualizar avaliações registradas
        self.sistema.user = Admin()
        self.sistema.login = True
        assert self.sistema.verificar_avaliacoes()

        # CT4 - Deletar as avaliações com sucesso
        assert self.sistema.deletar_avaliacoes()

        # CT5 - Deletar as avaliações sem existirem
        assert not self.sistema.deletar_avaliacoes()

        # CT6 - Verificar avaliações sem ter recebido nenhuma
        assert not self.sistema.verificar_avaliacoes()

    
    # CNT7 - Visualizar informações de paciente
    @pytest.mark.run(order=9) 
    def test_visualizar_informacoes_paciente(self):
        
        # CT1 - Visualizar informações de um paciente existente
        self.sistema.user = Dentista()
        assert self.sistema.ver_historico_paciente(cpf="admin")
        self.sistema.user = Admin()
        assert self.sistema.ver_historico_paciente(cpf="admin")
        self.sistema.user = Paciente()
        assert self.sistema.ver_registros()

        # CT2 - Tentativa de visualizar paciente inexistente
        self.sistema.user = Dentista()
        assert not self.sistema.ver_historico_paciente(cpf="0129102")
        self.sistema.user = Admin()
        assert not self.sistema.ver_historico_paciente(cpf="af3f3f3")

        # CT3 - Tentativa de visualizar paciente sem historico
        self.sistema.user = Dentista()
        assert not self.sistema.ver_historico_paciente(cpf="teste")
        self.sistema.user = Admin()
        assert not self.sistema.ver_historico_paciente(cpf="teste")
        self.sistema.fazer_login(tipo_usuario="Paciente",cpf="teste",senha="teste123")
        assert not self.sistema.ver_registros()

    
    # CNT8 - Realização de Pagamento
    @pytest.mark.run(order=7)
    def test_realizar_pagamento(self):
        self.sistema.user = Admin()

        # CT1 - Anexar pagamento com sucesso
        assert self.sistema.anexa_pagamento(cpf="admin",valor=50.75,moeda="real")
        assert self.sistema.anexa_pagamento(cpf="teste",valor="10",moeda="euro")

        # CT2 - Tentativa de anexar pagamento para paciente inexistente
        assert not self.sistema.anexa_pagamento(cpf="-920313b",valor = 50,moeda = "dolar")

        # CT3 - Tentativa de anexar pagamento sem ser Atendente
        self.sistema.user = Dentista()
        assert not self.sistema.anexa_pagamento(cpf="teste",valor = 50,moeda = "dolar")
        self.sistema.user = Paciente()
        assert not self.sistema.anexa_pagamento(cpf="teste",valor = 50,moeda = "dolar")

        # CT3 - Tentativa de realizar pagamento sem ter valor suficiente
        assert not self.sistema.realizar_pagamento(pagamento=50.1,tipo_pagamento="cartao de debito")
        assert not self.sistema.realizar_pagamento(pagamento="50",tipo_pagamento="cartao de credito")
        assert not self.sistema.realizar_pagamento(pagamento=50,tipo_pagamento="dinheiro")

        # CT4 - Tentativa de realizar pagamento sem selecionar tipo de pagamento
        assert not self.sistema.realizar_pagamento(pagamento=60)

        # CT5 - Realizar pagamento sem estar logado
        self.sistema.login = False
        assert not self.sistema.realizar_pagamento(pagamento=51,tipo_pagamento="dinheiro")

        # CT6 - Realizar pagamento com sucesso
        self.sistema.login = True
        assert self.sistema.realizar_pagamento(pagamento=51,tipo_pagamento="dinheiro")

        # CT7 - Realizar pagamento que não existe 
        assert not self.sistema.realizar_pagamento(pagamento=51,tipo_pagamento="fiado")

    
    # CNT9 - Manipulação Histórico paciente
    @pytest.mark.run(order=8)
    def test_adicionar_historico_paciente(self):
        self.sistema.user = Dentista()

        # CT1 - Adicionar anexo ao paciente com sucesso
        assert self.sistema.adicionar_anexo(cpf="admin",tipo="receita",info="remedio antibiótico",infoadd="12 em 12 horas")

        # CT2 - Adicionar anexo ao paciente inexistente
        assert not self.sistema.adicionar_anexo(cpf="-193932r",tipo="atestado",info="cirurgia odontológica",infoadd="15 dias de repouso")
        
        # CT2 - Adicionar anexo ao paciente inexistente
        self.sistema.user = Admin()
        assert not self.sistema.adicionar_anexo(cpf="teste",tipo="atestado",info="cirurgia odontológica",infoadd="15 dias de repouso")

        # CT3 - Arquivar consulta sem ser Dentista
        self.sistema.agendar_consulta(cpf="admin",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="reagentamento")
        assert not self.sistema.arquivar_consulta(cpf="admin")
        
        # CT4 - Arquivar consulta existente
        self.sistema.user = Dentista()
        assert self.sistema.arquivar_consulta(cpf="admin")

        # CT4 - Arquivar consulta inexistente
        assert not self.sistema.arquivar_consulta(cpf="admin")

    
    # CNT10 - Visualizar informações de dentista
    @pytest.mark.run(order=10) 
    def test_visualizar_informacoes_dentista(self):

        # CT1 - Visualizar informações dos dentistas cadastrados
        self.sistema.user = Admin()
        assert self.sistema.visualizar_dentistas()

        # CT2 - Visualizar informações de um dentista existente
        assert self.sistema.visualizar_dentista(cpf="teste")

        # CT3 - Tentativa de visualizar dentista inexistente
        assert not self.sistema.visualizar_dentista(cpf="-1291839j")

        # CT4 - Tentativa de visualizar agenda de dentista existente
        self.sistema.agendar_consulta(cpf="admin",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="reagentamento")
        self.sistema.agendar_consulta(cpf="teste",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="reagentamento")
        r = self.sistema.ver_agenda_dentista(cpf="admin")
        assert r
        self.sistema.user = Dentista()
        assert self.sistema.ver_agenda()
        assert (self.sistema.ver_agenda() == r)

        # CT5 - Tentativa de visualizar agenda de dentista existente mas sem consultas registradas
        self.sistema.cancelar_consulta(cpf="admin")
        self.sistema.cancelar_consulta(cpf="teste")
        self.sistema.fazer_login(tipo_usuario="Dentista",cpf="teste",senha="teste123")
        assert  not self.sistema.ver_agenda_dentista(cpf="teste")
        assert  not self.sistema.ver_agenda()