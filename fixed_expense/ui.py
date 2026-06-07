from rich.align import Align
from rich.console import Console
from rich.table import Table


def mostrar_menu_gasto_fixo():
    """
    Exibe o menu de gastos fixos.
    :return: None.
    """
    console = Console()

    menu_gasto_fixo = Table(style = "#FF8C00", width = 40)
    menu_gasto_fixo.add_column("OPÇÕES", justify = "center")
    menu_gasto_fixo.add_row(Align.left("[1] Aluguel"))
    menu_gasto_fixo.add_row(Align.left("[2] Conta"))
    menu_gasto_fixo.add_row(Align.left("[3] Plano de Saúde"))
    menu_gasto_fixo.add_row(Align.left("[4] Transporte"))
    menu_gasto_fixo.add_section()
    menu_gasto_fixo.add_row(Align.left("[bold #FF8C00][5] Voltar para o Menu Principal[/]"))

    console.print(menu_gasto_fixo)


def mostrar_menu_conta():
    """
    Exibe o menu de tipos de conta.
    :return: None.
    """
    console = Console()

    menu_conta = Table(style = "#FF8C00", width = 30)
    menu_conta.add_column("TIPO DE CONTA", justify = "center")
    menu_conta.add_row(Align.left("[1] Água"))
    menu_conta.add_row(Align.left("[2] Luz"))
    menu_conta.add_row(Align.left("[3] Internet"))
    menu_conta.add_row(Align.left("[4] Outros"))

    console.print(menu_conta)


def mostrar_menu_plano():
    """
    Exibe o menu de tipos de plano de saúde.
    :return: None.
    """
    console = Console()

    menu_plano = Table(style = "#FF8C00", width = 30)
    menu_plano.add_column("TIPO DE PLANO", justify = "center")
    menu_plano.add_row(Align.left("[1] Individual"))
    menu_plano.add_row(Align.left("[2] Familiar"))
    menu_plano.add_row(Align.left("[3] Empresarial"))
    menu_plano.add_row(Align.left("[4] Outros"))

    console.print(menu_plano)


def mostrar_menu_servicos():
    """
    Exibe o menu de tipos de serviço de transporte.
    :return: None.
    """
    console = Console()

    menu_servicos = Table(style = "#FF8C00", width = 30)
    menu_servicos.add_column("TIPO DE SERVIÇO", justify = "center")
    menu_servicos.add_row(Align.left("[1] Combustível"))
    menu_servicos.add_row(Align.left("[2] Manutenção"))
    menu_servicos.add_row(Align.left("[3] Transporte Público"))
    menu_servicos.add_row(Align.left("[4] Outros"))

    console.print(menu_servicos)