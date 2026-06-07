from revenue.base import Receita


class Salario(Receita):
    """
    Representa receitas financeiras mensais provenientes de vínculo empregatício.
    :param valor: Salário em reais.
    :param mes: Mês de competência (1 a 12).
    :param origem: Empresa pagadora.
    :param cargo: Cargo de ocupação na empresa.
    """
    def __init__(self, valor, mes, origem, cargo):
        super().__init__(valor, mes, origem)
        self.__cargo = str(cargo)


    @property
    def cargo(self) -> str: return self.__cargo


class RendaExtra(Receita):
    """
    Representa receitas financeiras provenientes de atividades autônomas através de investimentos.
    :param valor: Valor obtido em reais.
    :param mes: Mês de competência (1 a 12).
    :param origem: Responsável pelo pagamento.
    :param custo: Investimento realizado.
    """
    def __init__(self, valor, mes, origem, custo):
        super().__init__(valor, mes, origem)
        self.__custo = float(custo)


    @property
    def custo(self) -> float: return self.__custo


class Freelance(Receita):
    """
    Representa receitas financeiras provenientes de atividades autônomas.
    O valor total é calculado com base no **valor_hora** e **horas_trabalhadas**.
    :param mes: Mês de competência (1 a 12).
    :param origem: Responsável pelo pagamento.
    :param valor_hora: Valor da hora trabalhada em reais.
    :param horas_trabalhadas: Quantidade de horas trabalhadas.
    """
    def __init__(self, mes, origem, valor_hora, horas_trabalhadas):
        super().__init__(valor_hora * horas_trabalhadas, mes, origem)
        self.__valor_hora = float(valor_hora)
        self.__horas_trabalhadas = int(horas_trabalhadas)


    @property
    def valor_hora(self) -> float: return self.__valor_hora


    @property
    def horas_trabalhadas(self) -> int: return self.__horas_trabalhadas