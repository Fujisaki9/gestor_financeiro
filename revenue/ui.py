from rich.align import Align
from rich.console import Console
from rich.table import Table


def mostrar_menu_receita():
    """
    Exibe o menu de opções para o usuário escolher o tipo de receita que deseja registrar.
    :return: None.
    """
    console = Console()
    menu_receita = Table(style = "#FF8C00", width = 40)
    menu_receita.add_column("OPÇÕES", justify = 'center')
    menu_receita.add_row(Align.left("[1] Salário"))
    menu_receita.add_row(Align.left("[2] Renda Extra"))
    menu_receita.add_row(Align.left("[3] Freelancer"))
    menu_receita.add_section()
    menu_receita.add_row(Align.left("[bold #FF8C00][4] Voltar para o Menu Principal[/]"))

    console.print(menu_receita)