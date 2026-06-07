from abc import ABC


class Receita(ABC):
    """
    Classe base para registro de receitas financeiras.
    Subclasses: Salário, RendaExtra e Freelancer.
    :param valor: Valor recebido em reais.
    :param mes: Mês (1 a 12).
    :param origem: Fonte ou responsável pelo pagamento da receita.
    """
    def __init__(self, valor, mes, origem):
        self.__valor = float(valor)
        self.__mes = int(mes)
        self.__origem = str(origem)


    @property
    def valor(self) -> float: return self.__valor


    @valor.setter
    def valor(self, valor_novo): self.__valor = float(valor_novo)


    @property
    def mes(self) -> int: return self.__mes


    @mes.setter
    def mes(self, mes_novo): self.__mes = int(mes_novo)


    @property
    def origem(self) -> str: return self.__origem


    @origem.setter
    def origem(self, origem_nova): self.__origem = str(origem_nova)
