class Investimento:
    """
    Representa os investimentos financeiros mensais.
    :param valor_investido: Valor investido em reais.
    :param mes_investimento: Mês de competência (1 a 12).
    :param tipo_investimento: Tipo de investimento (poupança, reserva de emergência, tesouro direto).
    :param entidade: Banco ou corretora onde o investimento está aplicado.
    """
    def __init__(self, valor_investido, mes_investimento, tipo_investimento, entidade):
        self.__valor_investido = float(valor_investido)
        self.__mes_investimento = int(mes_investimento)
        self.__tipo_investimento = str(tipo_investimento)
        self.__entidade = str(entidade)


    @property
    def valor_investido(self) -> float: return self.__valor_investido


    @property
    def mes_investimento(self) -> int: return self.__mes_investimento


    @property
    def tipo_investimento(self) -> str: return self.__tipo_investimento


    @property
    def entidade(self) -> str: return self.__entidade