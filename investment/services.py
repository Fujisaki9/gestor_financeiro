from rich import print as rprint

from investment.models import Investimento
from investment.repository import inserir_registro_investimento
from investment.ui import  mostrar_menu_investimento, mostrar_tipos_investimento
from shared.enums import TipoInvestimento
from utils.console import limpar_console
from utils.validators import validar_float, validar_integer, validar_mes


def registrar_investimento():
    """
    Registra um novo investimento.
    :return: None.
    """
    while True:
        limpar_console()
        mostrar_menu_investimento()
        opcao = validar_integer("Escolha uma opção: ")
        match opcao:
            case 1:
                valor = validar_float("Valor do investimento: R$ ")
                mes = validar_mes("Mês: ")
                tipo_investimento = escolher_tipo_investimento()
                entidade = input("Instituição: ").strip().title()
                novo_registro = Investimento(valor, mes, tipo_investimento, entidade)
                inserir_registro_investimento(novo_registro)
            case 2:
                break
            case _:
                rprint("[bold red]Insira um comando válido![/]")


def escolher_tipo_investimento():
    """
    Exibe as opções de tipos de investimento e retorna a escolha do usuário.
    :return: O tipo de investimento escolhido.
    """
    mostrar_tipos_investimento()
    while True:
        opcao = validar_integer("Escolha o tipo de investimento: ")
        match opcao:
            case 1:
                return TipoInvestimento.POUPANCA.value
            case 2:
                return TipoInvestimento.RESERVA.value
            case 3:
                return TipoInvestimento.ACOES.value
            case 4:
                return TipoInvestimento.OUTROS.value
            case _:
                rprint("[bold red]Insira um comando válido![/]")