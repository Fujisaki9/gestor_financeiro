from abc import ABC


class Gasto(ABC):
    """
    Classe base para registro de gastos mensais.
    :param valor_gasto: Valor gasto em reais.
    :param mes: Mês de competência (1 a 12).
    :param origem: Fonte ou responsável pelo gasto.
    :param forma_pagamento: Dinheiro, PIX, boleto, cartão.
    """
    def __init__(self, valor_gasto, mes, origem, forma_pagamento):
        self.__valor_gasto = float(valor_gasto)
        self.__mes = int(mes)
        self.__origem = str(origem)
        self.__forma_pagamento = str(forma_pagamento)


    @property
    def valor_gasto(self) -> float: return self.__valor_gasto


    @property
    def mes(self) -> int: return self.__mes


    @property
    def origem(self) -> str: return self.__origem


    @property
    def forma_pagamento(self) -> str: return self.__forma_pagamento
