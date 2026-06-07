from shared.expense import Gasto


class Alimentacao(Gasto):
    """
    Representa os gastos com alimentação.
    :param valor_gasto: Valor gasto em reais.
    :param mes: Mês de competência (1 a 12).
    :param origem: Local onde o gasto foi realizado.
    :param forma_pagamento: Forma de pagamento utilizada.
    :param tipo_alimentacao: Tipo de alimentação (supermercado, restaurante, delivery).
    """
    def __init__(self, valor_gasto, mes, origem, forma_pagamento, tipo_alimentacao):
        super().__init__(valor_gasto, mes, origem, forma_pagamento)
        self.__tipo_alimentacao = str(tipo_alimentacao)


    @property
    def tipo_alimentacao(self) -> str: return self.__tipo_alimentacao


class Lazer(Gasto):
    """
    Representa os gastos com lazer e entretenimento.
    :param valor_gasto: Valor gasto em reais.
    :param mes: Mês de competência (1 a 12).
    :param origem: Local onde o gasto foi realizado.
    :param forma_pagamento: Forma de pagamento utilizada.
    :param tipo_lazer: Tipo de lazer (cinema, viagem, jogos, academia).
    """
    def __init__(self, valor_gasto, mes, origem, forma_pagamento, tipo_lazer):
        super().__init__(valor_gasto, mes, origem, forma_pagamento)
        self.__tipo_lazer = str(tipo_lazer)


    @property
    def tipo_lazer(self) -> str: return self.__tipo_lazer


class Farmacia(Gasto):
    """
    Representa os gastos com farmácia.
    :param valor_gasto: Valor gasto em reais.
    :param mes: Mês de competência (1 a 12).
    :param origem: Local onde o gasto foi realizado.
    :param forma_pagamento: Forma de pagamento utilizada.
    :param tipo_farmacia: Tipo de produto adquirido (medicamento, cosmético, suplemento).
    """
    def __init__(self, valor_gasto, mes, origem, forma_pagamento, tipo_farmacia):
        super().__init__(valor_gasto, mes, origem, forma_pagamento)
        self.__tipo_farmacia = str(tipo_farmacia)


    @property
    def tipo_farmacia(self) -> str: return self.__tipo_farmacia


class Diversos(Gasto):
    """
    Representa os gastos que não se enquadram em nenhuma categoria específica.
    :param valor_gasto: Valor gasto em reais.
    :param mes: Mês de competência (1 a 12).
    :param origem: Local onde o gasto foi realizado.
    :param forma_pagamento: Forma de pagamento utilizada.
    :param descricao_gasto: Descrição do gasto realizado.
    """
    def __init__(self, valor_gasto, mes, origem, forma_pagamento, descricao_gasto):
        super().__init__(valor_gasto, mes, origem, forma_pagamento)
        self.__descricao_gasto = str(descricao_gasto)


    @property
    def descricao_gasto(self) -> str: return self.__descricao_gasto