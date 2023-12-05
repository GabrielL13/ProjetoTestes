import pytest
from Sistema import Sistema
from Admin import Admin
from Paciente import Paciente
from Dentista import Dentista
from datetime import datetime

class TestSistema():

    admin = Admin()
    paciente = Paciente()
    dentista = Dentista()
    
    # CNT1 - Cadastro de Paciente
    @pytest.mark.run(order=1)
    def test_cadastro_paciente(self):

        # CT1 - Cadastro de um novo paciente com informações válidas
        assert self.admin.criar_ficha(nome="Teste1", cpf="teste", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        
        # CT2 - Tentativa de cadastro de um paciente com CPF já existente
        assert not self.admin.criar_ficha(nome="Teste2", cpf="teste", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")
        
        # CT3 - Tentativa de cadastro de um paciente sem preencher algum campo
        assert not self.admin.criar_ficha(nome="Teste3", cpf="-99999999", senha="teste123",
                                                rg="1234567", cartaoSus="sus123", rua="ruateste",
                                                bairro="bairroteste", cidade="cidadeteste", numero="1", cep="cep123",
                                                referencia="semref", data_de_nascimento=datetime.now(),
                                                estado_civil="estado", tipo_sanguineo="O+", nacionalidade="paisteste",
                                                sexo="sexoteste0", info_adicionais="add")
        
        # CT4 - Atualizar cadastro de paciente existente
        assert self.admin.atualizar_cadastro(nome="TesteAtualiza1", cpf="teste", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")

        # CT5 - Atualizar cadastro de paciente inexistente
        assert not self.admin.atualizar_cadastro(nome="TesteAtualiza2", cpf="0909091029103", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")

    # CNT2 - Cadastro de Dentista
    @pytest.mark.run(order=2)
    def test_cadastro_dentista(self):


        # CT1 - Cadastro de um novo paciente com informações válidas
        assert self.admin.criar_ficha_dentista(crm="crmteste",estado="estado",nome="Teste1", cpf="teste", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        
        # CT2 - Tentativa de cadastro de um paciente com CPF já existente
        assert not self.admin.criar_ficha_dentista(crm="crmteste",estado="estado",nome="Teste2", cpf="teste", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")
        
        # CT3 - Tentativa de cadastro de um paciente sem preencher algum campo
        assert not self.admin.criar_ficha_dentista(crm="crmteste",estado="estado",nome="Teste3", cpf="-99999999", senha="teste123",
                                                rg="1234567", cartaoSus="sus123", rua="ruateste",
                                                bairro="bairroteste", cidade="cidadeteste", numero="1", cep="cep123",
                                                referencia="semref", data_de_nascimento=datetime.now(),
                                                estado_civil="estado", tipo_sanguineo="O+", nacionalidade="paisteste",
                                                sexo="sexoteste0", info_adicionais="add")
   

   # CNT3 - Cadastro de Atendente
    @pytest.mark.run(order=3)
    def test_cadastro_atendente(self):

        # CT1 - Cadastro de um novo paciente com informações válidas
        assert self.admin.criar_ficha_atendente(nome="Teste1", cpf="teste", senha="teste123",
                                               telefone="12345678", rg="1234567", cartaoSus="sus123",
                                               rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                               numero="1", cep="cep123", referencia="semref",
                                               data_de_nascimento=datetime.now(), estado_civil="estado",
                                               tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                               info_adicionais="add")
        
        # CT2 - Tentativa de cadastro de um paciente com CPF já existente
        assert not self.admin.criar_ficha_atendente(nome="Teste2", cpf="teste", senha="teste123",
                                                telefone="12345678", rg="1234567", cartaoSus="sus123",
                                                rua="ruateste", bairro="bairroteste", cidade="cidadeteste",
                                                numero="1", cep="cep123", referencia="semref",
                                                data_de_nascimento=datetime.now(), estado_civil="estado",
                                                tipo_sanguineo="O+", nacionalidade="paisteste", sexo="sexoteste0",
                                                info_adicionais="add")
        
        # CT3 - Tentativa de cadastro de um paciente sem preencher algum campo
        assert not self.admin.criar_ficha_atendente(nome="Teste3", cpf="-99999999", senha="teste123",
                                                rg="1234567", cartaoSus="sus123", rua="ruateste",
                                                bairro="bairroteste", cidade="cidadeteste", numero="1", cep="cep123",
                                                referencia="semref", data_de_nascimento=datetime.now(),
                                                estado_civil="estado", tipo_sanguineo="O+", nacionalidade="paisteste",
                                                sexo="sexoteste0", info_adicionais="add")
        
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
        assert self.admin.agendar_consulta(cpf="teste",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="consulta_teste1")
        
        # CT2 - Tentativa de marcar consulta sem cadastro
        assert not self.admin.agendar_consulta(cpf="admin",data=datetime.now()
                                    ,nome_dentista="admin",cpf_dentista="admin",descricao="consulta_teste1")
        
        # CT3 - Tentativa de marcar consulta que já existe (reagendamento)
        assert self.admin.agendar_consulta(cpf="teste",data=datetime.now()
                                    ,nome_dentista="teste",cpf_dentista="admin",descricao="reagentamento")
        
        # CT4 - Cancelar consulta existente
        assert self.admin.cancelar_consulta_admin(cpf="teste",cpf_dentista="teste")
        assert self.dentista.cancelar_consulta(cpf="teste")

        # CT5 - Cancelar consulta inexistente de um dentista inexistente
        assert not self.admin.cancelar_consulta_admin(cpf="-10390193",cpf_dentista="admin")

        # CT6 - Cancelar consulta inexistente de um dentista paciente
        assert not self.admin.cancelar_consulta_admin(cpf="teste",cpf_dentista="-090909")