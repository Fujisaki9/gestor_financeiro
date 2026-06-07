from rich.align import Align
from rich.console import Console
from rich.table import Table


def mostrar_menu_investimento():
    """
    Exibe um menu de opções
    :return: None.
    """
    console = Console()
    menu = Table(style="#FF8C00", width=40)
    menu.add_column("OPÇÕES", justify="center")
    menu.add_row(Align.left("[1] Registrar Investimento"))
    menu.add_section()
    menu.add_row(Align.left("[bold #FF8C00][2] Voltar ao menu principal[/]"))
    console.print(menu)


def mostrar_tipos_investimento():
    """
    Exibe o menu de tipos de investimento.
    :return: None.
    """
    console = Console()

    menu_investimento = Table(style="#FF8C00", width=30)
    menu_investimento.add_column("TIPOS DE INVESTIMENTO", justify = "center")
    menu_investimento.add_row(Align.left("[1] Poupança"))
    menu_investimento.add_row(Align.left("[2] Reserva de Emergência"))
    menu_investimento.add_row(Align.left("[3] Ações"))
    menu_investimento.add_row(Align.left("[4] Outros"))

    console.print(menu_investimento)