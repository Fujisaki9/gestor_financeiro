from rich.align import Align
from rich.console import Console
from rich.table import Table


def mostrar_menu_gastos_variaveis():
    """
    Exibe o menu de opções de gastos variáveis.
    :return: None.
    """
    console = Console()

    menu_gasto_variavel = Table(style="#FF8C00", width=40)
    menu_gasto_variavel.add_column("OPÇÕES", justify="center")
    menu_gasto_variavel.add_row(Align.left("[1] Alimentação"))
    menu_gasto_variavel.add_row(Align.left("[2] Lazer"))
    menu_gasto_variavel.add_row(Align.left("[3] Farmácia"))
    menu_gasto_variavel.add_row(Align.left("[4] Diversos"))
    menu_gasto_variavel.add_section()
    menu_gasto_variavel.add_row(Align.left("[bold #FF8C00][5] Voltar para o Menu Principal[/]"))

    console.print(menu_gasto_variavel)


def mostrar_tipos_alimentacao():
    """
    Exibe o menu de tipos de gastos relacionados à alimentação.
    :return: None.
    """
    console = Console()

    menu_alimentacao = Table(style="#FF8C00", width=30)
    menu_alimentacao.add_column("TIPOS DE GASTO", justify="center")
    menu_alimentacao.add_row(Align.left("[1] Supermercado"))
    menu_alimentacao.add_row(Align.left("[2] Restaurante"))
    menu_alimentacao.add_row(Align.left("[3] Delivery"))
    menu_alimentacao.add_row(Align.left("[4] Outros"))

    console.print(menu_alimentacao)


def mostrar_tipos_lazer():
    """
    Exibe o menu de tipos de gastos relacionados ao lazer.
    :return: None.
    """
    console = Console()

    menu_lazer = Table(style="#FF8C00", width=30)
    menu_lazer.add_column("TIPOS DE LAZER ", justify="center")
    menu_lazer.add_row(Align.left("[1] Shopping"))
    menu_lazer.add_row(Align.left("[2] Viagem"))
    menu_lazer.add_row(Align.left("[3] Academia"))
    menu_lazer.add_row(Align.left("[4] Outros"))

    console.print(menu_lazer)


def mostrar_tipos_farmacia():
    """
    Exibe o menu de tipos de gastos relacionados à farmácia.
    :return: None.
    """
    console = Console()

    menu_farmacia = Table(style="#FF8C00", width=30)
    menu_farmacia.add_column("TIPOS DE PRODUTO ", justify="center")
    menu_farmacia.add_row(Align.left("[1] Medicamento"))
    menu_farmacia.add_row(Align.left("[2] Cosmético"))
    menu_farmacia.add_row(Align.left("[3] Suplemento"))
    menu_farmacia.add_row(Align.left("[4] Outros"))

    console.print(menu_farmacia)