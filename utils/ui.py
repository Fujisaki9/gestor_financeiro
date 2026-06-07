from rich.align import Align
from rich.console import Console
from rich.table import Table


def mostrar_menu_pagamento():
    """
    Exibe o menu de opções para o usuário escolher a forma de pagamento.
    :return: None.
    """
    console = Console()

    menu_pagamento = Table(style = "#FF8C00", width = 30)
    menu_pagamento.add_column("TIPO DE PAGAMENTO", justify = "center")
    menu_pagamento.add_row(Align.left("[1] Dinheiro"))
    menu_pagamento.add_row(Align.left("[2] PIX"))
    menu_pagamento.add_row(Align.left("[3] Boleto"))
    menu_pagamento.add_row(Align.left("[4] Cartão"))
    menu_pagamento.add_row(Align.left("[5] Outros"))

    console.print(menu_pagamento)


def mostrar_menu_opcoes():
    """
    Exibe o menu de opções para o usuário escolher a ação desejada.
    :return: None.
    """
    console = Console()

    menu_opcoes = Table(title = "Gestor Financeiro", style = "#FF8C00", width = 35)
    menu_opcoes.add_column("OPÇÕES", justify = "center")
    menu_opcoes.add_row(Align.left("[1] Registrar Receita"))
    menu_opcoes.add_row(Align.left("[2] Registrar Gasto Fixo"))
    menu_opcoes.add_row(Align.left("[3] Registrar Gasto Variável"))
    menu_opcoes.add_row(Align.left("[4] Registrar Investimento"))
    menu_opcoes.add_row(Align.left("[5] Gerar Relatório"))
    menu_opcoes.add_row(Align.left("[bold #FF8C00][6] Sair[/]"))

    console.print(menu_opcoes)