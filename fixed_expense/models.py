from shared.expense import Gasto


class Aluguel(Gasto):
    """
    Representa os gastos mensais com moradia.
    :param valor_gasto: Valor do aluguel em reais.
    :param mes: Mês de competência (1 a 12).
    :param origem: Nome do proprietário do imóvel.
    :param forma_pagamento: Forma de pagamento utilizada.
    :param endereco_imovel: Endereço do imóvel alugado.
    :param numero_imovel: Número ou complemento do imóvel.
    """
    def __init__(self, valor_gasto, mes, origem, forma_pagamento, endereco_imovel, numero_imovel):
        super().__init__(valor_gasto, mes, origem, forma_pagamento)
        self.__endereco_imovel = str(endereco_imovel)
        self.__numero_imovel = str(numero_imovel)


    @property
    def endereco_imovel(self) -> str: return self.__endereco_imovel


    @property
    def numero_imovel(self) -> str: return self.__numero_imovel


class Conta(Gasto):
    """
    Representa os gastos mensais com contas de serviços essenciais.
    :param valor_gasto: Valor da conta em reais.
    :param mes: Mês de competência (1 a 12).
    :param origem: Nome da empresa prestadora do serviço.
    :param forma_pagamento: Forma de pagamento utilizada.
    :param tipo_conta: Tipo de serviço contratado (água, luz, internet).
    """
    def __init__(self, valor_gasto, mes, origem, forma_pagamento, tipo_conta):
        super().__init__(valor_gasto, mes, origem, forma_pagamento)
        self.__tipo_conta = str(tipo_conta)


    @property
    def tipo_conta(self) -> str: return self.__tipo_conta


class PlanoSaude(Gasto):
    """
    Representa os gastos mensais com plano de saúde.
    :param valor_gasto: Valor da mensalidade em reais.
    :param mes: Mês de competência (1 a 12).
    :param origem: Nome da operadora do plano.
    :param forma_pagamento: Forma de pagamento utilizada.
    :param tipo_plano: Tipo de cobertura contratada (individual, familiar, empresarial).
    """
    def __init__(self, valor_gasto, mes, origem, forma_pagamento, tipo_plano):
        super().__init__(valor_gasto, mes, origem, forma_pagamento)
        self.__tipo_plano = str(tipo_plano)


    @property
    def tipo_plano(self) -> str: return self.__tipo_plano


class Transporte(Gasto):
    """
    Representa os gastos mensais com transporte.
    :param valor_gasto: Valor gasto em reais.
    :param mes: Mês de competência (1 a 12).
    :param origem: Local ou empresa onde o serviço foi realizado.
    :param forma_pagamento: Forma de pagamento utilizada.
    :param tipo_servico: Tipo de serviço utilizado (combustível, manutenção, transporte público, pedágio).
    """
    def __init__(self, valor_gasto, mes, origem, forma_pagamento, tipo_servico):
        super().__init__(valor_gasto, mes, origem, forma_pagamento)
        self.__tipo_servico = str(tipo_servico)


    @property
    def tipo_servico(self) -> str: return self.__tipo_servico