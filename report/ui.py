from rich.align import Align
from rich.console import Console
from rich.table import Table

from utils.formatters import converter_mes, formatar_valor


def mostrar_relatorio_salario(relatorio):
    """
    Exibe o relatório de salário.
    :param relatorio: Lista de objetos Salario.
    :return: None.
    """
    console = Console()
    relatorio_salario = Table(title = "Relatório de Salário", style = "#FF8C00")

    relatorio_salario.add_column("Mês", justify = "center")
    relatorio_salario.add_column("Empresa", justify = "center")
    relatorio_salario.add_column("Cargo", justify = "center")
    relatorio_salario.add_column("Valor", justify="center")

    soma = sum(registro.valor for registro in relatorio)
    for registro in relatorio:
        relatorio_salario.add_row(converter_mes(registro.mes),
                                  Align.left(registro.origem),
                                  Align.left(registro.cargo),
                                  Align.left(f"{formatar_valor(registro.valor)}"))
    relatorio_salario.add_section()
    relatorio_salario.add_row("", "", "[bold #FF8C00]Valor Total[/]",
                              Align.right(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))

    console.print(relatorio_salario)


def mostrar_relatorio_renda_extra(relatorio):
    """
    Exibe o relatório de renda extra.
    :param relatorio: Lista de objetos RendaExtra.
    :return: None.
    """
    console = Console()
    relatorio_renda_extra = Table(title = "Relatório de Renda Extra", style = "#FF8C00")

    relatorio_renda_extra.add_column("Mês", justify = "center")
    relatorio_renda_extra.add_column("Atividade", justify = "center")
    relatorio_renda_extra.add_column("Custo", justify = "center")
    relatorio_renda_extra.add_column("Valor", justify="center")

    soma = sum(registro.valor for registro in relatorio)
    for registro in relatorio:
        relatorio_renda_extra.add_row(converter_mes(registro.mes),
                                      Align.left(registro.origem),
                                      Align.left(formatar_valor(registro.custo)),
                                      Align.left(f"{formatar_valor(registro.valor)}"))
    relatorio_renda_extra.add_section()
    relatorio_renda_extra.add_row("", "", "[bold #FF8C00]Valor Total[/]",
                                  Align.right(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))
    console.print(relatorio_renda_extra)


def mostrar_relatorio_freelance(relatorio):
    """
    Exibe o relatório de freelance.
    :param relatorio: Lista de objetos Freelance.
    :return: None.
    """
    console = Console()
    relatorio_freelance = Table(title = "Relatório de Freelance", style = "#FF8C00")

    relatorio_freelance.add_column("Mês", justify = "center")
    relatorio_freelance.add_column("Contratante", justify = "center")
    relatorio_freelance.add_column("Horas Trabalhadas", justify="center")
    relatorio_freelance.add_column("Preço/Hora", justify = "center")
    relatorio_freelance.add_column("Valor", justify="center")

    soma = sum(registro.valor for registro in relatorio)
    for registro in relatorio:
        relatorio_freelance.add_row(converter_mes(registro.mes),
                                    Align.left(registro.origem),
                                    str(registro.horas_trabalhadas),
                                    Align.left(f"{formatar_valor(registro.valor_hora)}"),
                                    Align.left(f"{formatar_valor(registro.valor)}"))
    relatorio_freelance.add_section()
    relatorio_freelance.add_row("", "", "", "[bold #FF8C00]Valor Total[/]",
                                Align.right(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))

    console.print(relatorio_freelance)


def mostrar_relatorio_aluguel(relatorio):
    """
    Exibe o relatório de aluguel.
    :param relatorio: Lista de objetos Aluguel.
    :return: None.
    """
    console = Console(width = 110)
    relatorio_aluguel = Table(title = "Relatório de Aluguel", style = "#FF8C00")

    relatorio_aluguel.add_column("Mês", justify = "center")
    relatorio_aluguel.add_column("Proprietário", justify = "center")
    relatorio_aluguel.add_column("Endereço do Imóvel", justify = "center")
    relatorio_aluguel.add_column("Número do Imóvel", justify = "center")
    relatorio_aluguel.add_column("Forma de Pagamento", justify="center")
    relatorio_aluguel.add_column("Valor", justify="center")

    soma = sum(registro.valor_gasto for registro in relatorio)
    for registro in relatorio:
        relatorio_aluguel.add_row(converter_mes(registro.mes),
                                  Align.left(registro.origem),
                                  Align.left(registro.endereco_imovel),
                                  registro.numero_imovel,
                                  registro.forma_pagamento,
                                  Align.left(f"{formatar_valor(registro.valor_gasto)}"))
    relatorio_aluguel.add_section()
    relatorio_aluguel.add_row("", "", "", "", "[bold #FF8C00]Valor Total[/]",
                              Align.right(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))

    console.print(relatorio_aluguel)


def mostrar_relatorio_conta(relatorio):
    """
    Exibe o relatório de contas.
    :param relatorio: Lista de objetos Conta.
    :return: None.
    """
    console = Console()
    relatorio_conta = Table(title = "Relatório de Contas", style = "#FF8C00")

    relatorio_conta.add_column("Mês", justify = "center")
    relatorio_conta.add_column("Empresa", justify = "center")
    relatorio_conta.add_column("Tipo de Conta", justify = "center")
    relatorio_conta.add_column("Forma de Pagamento", justify="center")
    relatorio_conta.add_column("Valor", justify="center")

    soma = sum(registro.valor_gasto for registro in relatorio)
    for registro in relatorio:
        relatorio_conta.add_row(converter_mes(registro.mes),
                                  Align.left(registro.origem),
                                  registro.tipo_conta,
                                  registro.forma_pagamento,
                                  Align.left(f"{formatar_valor(registro.valor_gasto)}"))
    relatorio_conta.add_section()
    relatorio_conta.add_row("", "", "", "[bold #FF8C00]Valor Total[/]",
                              Align.right(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))

    console.print(relatorio_conta)


def mostrar_relatorio_plano_saude(relatorio):
    """
    Exibe o relatório de plano de saúde.
    :param relatorio: Lista de objetos PlanoSaude.
    :return: None.
    """
    console = Console()
    relatorio_plano_saude = Table(title = "Relatório de Plano de Saúde", style = "#FF8C00")

    relatorio_plano_saude.add_column("Mês", justify = "center")
    relatorio_plano_saude.add_column("Operadora", justify = "center")
    relatorio_plano_saude.add_column("Tipo de Plano", justify = "center")
    relatorio_plano_saude.add_column("Forma de Pagamento", justify="center")
    relatorio_plano_saude.add_column("Valor", justify="center")

    soma = sum(registro.valor_gasto for registro in relatorio)
    for registro in relatorio:
        relatorio_plano_saude.add_row(converter_mes(registro.mes),
                                      Align.left(registro.origem),
                                      registro.tipo_plano,
                                      registro.forma_pagamento,
                                      Align.left(f"{formatar_valor(registro.valor_gasto)}"))
    relatorio_plano_saude.add_section()
    relatorio_plano_saude.add_row("", "", "", "[bold #FF8C00]Valor Total[/]",
                                  Align.right(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))

    console.print(relatorio_plano_saude)


def mostrar_relatorio_transporte(relatorio):
    """
    Exibe o relatório de transporte.
    :param relatorio: Lista de objetos Transporte.
    :return: None.
    """
    console = Console()
    relatorio_transporte = Table(title = "Relatório de Transporte", style = "#FF8C00")

    relatorio_transporte.add_column("Mês", justify = "center")
    relatorio_transporte.add_column("Empresa", justify = "center")
    relatorio_transporte.add_column("Tipo de Serviço", justify = "center")
    relatorio_transporte.add_column("Forma de Pagamento", justify="center")
    relatorio_transporte.add_column("Valor", justify="center")

    soma = sum(registro.valor_gasto for registro in relatorio)
    for registro in relatorio:
        relatorio_transporte.add_row(converter_mes(registro.mes),
                                      Align.left(registro.origem),
                                      registro.tipo_servico,
                                      registro.forma_pagamento,
                                      Align.left(f"{formatar_valor(registro.valor_gasto)}"))
    relatorio_transporte.add_section()
    relatorio_transporte.add_row("", "", "", "[bold #FF8C00]Valor Total[/]",
                                  Align.right(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))

    console.print(relatorio_transporte)


def mostrar_relatorio_alimentacao(relatorio):
    """
    Exibe o relatório de alimentação.
    :param relatorio: Lista de objetos Alimentacao.
    :return: None.
    """
    console = Console()
    relatorio_alimentacao = Table(title = "Relatório de Alimentação", style = "#FF8C00")

    relatorio_alimentacao.add_column("Mês", justify = "center")
    relatorio_alimentacao.add_column("Estabelecimento", justify = "center")
    relatorio_alimentacao.add_column("Tipo de Alimentação", justify = "center")
    relatorio_alimentacao.add_column("Forma de Pagamento", justify="center")
    relatorio_alimentacao.add_column("Valor", justify="center")

    soma = sum(registro.valor_gasto for registro in relatorio)
    for registro in relatorio:
        relatorio_alimentacao.add_row(converter_mes(registro.mes),
                                      Align.left(registro.origem),
                                      registro.tipo_alimentacao,
                                      registro.forma_pagamento,
                                      Align.left(f"{formatar_valor(registro.valor_gasto)}"))
    relatorio_alimentacao.add_section()
    relatorio_alimentacao.add_row("", "", "", "[bold #FF8C00]Valor Total[/]",
                                  Align.right(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))

    console.print(relatorio_alimentacao)


def mostrar_relatorio_lazer(relatorio):
    """
    Exibe o relatório de lazer.
    :param relatorio: Lista de objetos Lazer.
    :return: None.
    """
    console = Console()
    relatorio_lazer = Table(title = "Relatório de Lazer", style = "#FF8C00")

    relatorio_lazer.add_column("Mês", justify = "center")
    relatorio_lazer.add_column("Estabelecimento", justify = "center")
    relatorio_lazer.add_column("Tipo de Lazer", justify = "center")
    relatorio_lazer.add_column("Forma de Pagamento", justify="center")
    relatorio_lazer.add_column("Valor", justify="center")

    soma = sum(registro.valor_gasto for registro in relatorio)
    for registro in relatorio:
        relatorio_lazer.add_row(converter_mes(registro.mes),
                                      Align.left(registro.origem),
                                      registro.tipo_lazer,
                                      registro.forma_pagamento,
                                      Align.left(f"{formatar_valor(registro.valor_gasto)}"))
    relatorio_lazer.add_section()
    relatorio_lazer.add_row("", "", "", "[bold #FF8C00]Valor Total[/]",
                            Align.right(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))

    console.print(relatorio_lazer)


def mostrar_relatorio_farmacia(relatorio):
    """
    Exibe o relatório de farmácia.
    :param relatorio: Lista de objetos Farmacia.
    :return: None.
    """
    console = Console()
    relatorio_farmacia = Table(title = "Relatório de Farmácia", style = "#FF8C00")

    relatorio_farmacia.add_column("Mês", justify = "center")
    relatorio_farmacia.add_column("Estabelecimento", justify = "center")
    relatorio_farmacia.add_column("Tipo de Produto", justify = "center")
    relatorio_farmacia.add_column("Forma de Pagamento", justify="center")
    relatorio_farmacia.add_column("Valor", justify="center")

    soma = sum(registro.valor_gasto for registro in relatorio)
    for registro in relatorio:
        relatorio_farmacia.add_row(converter_mes(registro.mes),
                                      Align.left(registro.origem),
                                      registro.tipo_farmacia,
                                      registro.forma_pagamento,
                                      Align.left(f"{formatar_valor(registro.valor_gasto)}"))
    relatorio_farmacia.add_section()
    relatorio_farmacia.add_row("", "", "", "[bold #FF8C00]Valor Total[/]",
                               Align.right(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))

    console.print(relatorio_farmacia)


def mostrar_relatorio_diversos(relatorio):
    """
    Exibe o relatório de gastos diversos.
    :param relatorio: Lista de objetos Diversos.
    :return: None.
    """
    console = Console()
    relatorio_diversos = Table(title = "Relatório de Diversos", style = "#FF8C00")

    relatorio_diversos.add_column("Mês", justify = "center")
    relatorio_diversos.add_column("Estabelecimento", justify = "center")
    relatorio_diversos.add_column("Tipo de Gasto", justify = "center")
    relatorio_diversos.add_column("Forma de Pagamento", justify="center")
    relatorio_diversos.add_column("Valor", justify="center")

    soma = sum(registro.valor_gasto for registro in relatorio)
    for registro in relatorio:
        relatorio_diversos.add_row(converter_mes(registro.mes),
                                      Align.left(registro.origem),
                                      registro.descricao_gasto,
                                      registro.forma_pagamento,
                                      Align.left(f"{formatar_valor(registro.valor_gasto)}"))
    relatorio_diversos.add_section()
    relatorio_diversos.add_row("", "", "", "[bold #FF8C00]Valor Total[/]",
                               Align.right(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))

    console.print(relatorio_diversos)


def mostrar_relatorio_investimento(relatorio):
    """
    Exibe o relatório de investimentos.
    :param relatorio: Lista de objetos Investimento.
    :return: None.
    """
    console = Console()
    relatorio_investimento = Table(title = "Relatório de Investimentos", style = "#FF8C00")

    relatorio_investimento.add_column("Mês", justify = "center")
    relatorio_investimento.add_column("Tipo de Investimento", justify = "center")
    relatorio_investimento.add_column("Entidade", justify = "center")
    relatorio_investimento.add_column("Valor Investido", justify="center")

    soma = sum(registro.valor_investido for registro in relatorio)
    for registro in relatorio:
        relatorio_investimento.add_row(converter_mes(registro.mes_investimento),
                                      registro.tipo_investimento,
                                      registro.entidade,
                                      Align.left(f"{formatar_valor(registro.valor_investido)}"))
    relatorio_investimento.add_section()
    relatorio_investimento.add_row("", "", "[bold #FF8C00]Valor Total Investido[/]",
                                  Align.left(f"[bold #FF8C00]{formatar_valor(soma)}[/]"))

    console.print(relatorio_investimento)


def mostrar_menu_relatorio():
    """
    Exibe o menu de opções para o usuário escolher qual relatório deseja visualizar.
    :return: None.
    """
    console = Console()
    menu_relatorio = Table(style = "#FF8C00")

    menu_relatorio.add_column("Menu de Relatórios", justify = "center")

    menu_relatorio.add_row(Align.left("[01] Relatório de Salário"))
    menu_relatorio.add_row(Align.left("[02] Relatório de Renda Extra"))
    menu_relatorio.add_row(Align.left("[03] Relatório de Freelance"))
    menu_relatorio.add_row(Align.left("[04] Relatório de Aluguel"))
    menu_relatorio.add_row(Align.left("[05] Relatório de Contas"))
    menu_relatorio.add_row(Align.left("[06] Relatório de Plano de Saúde"))
    menu_relatorio.add_row(Align.left("[07] Relatório de Transporte"))
    menu_relatorio.add_row(Align.left("[08] Relatório de Alimentação"))
    menu_relatorio.add_row(Align.left("[09] Relatório de Lazer"))
    menu_relatorio.add_row(Align.left("[10] Relatório de Farmácia"))
    menu_relatorio.add_row(Align.left("[11] Relatório de Gastos Diversos"))
    menu_relatorio.add_row(Align.left("[12] Relatório de Investimentos"))
    menu_relatorio.add_section()
    menu_relatorio.add_row(Align.left("[bold #FF8C00][13] Voltar para o menu de opções[/]"))

    console.print(menu_relatorio)


def mostrar_opcao_relatorio():
    """
    Exibe o menu de opções para o usuário escolher qual relatório deseja visualizar.
    :return: None.
    """
    console = Console()
    menu_relatorio = Table(style = "#FF8C00")

    menu_relatorio.add_column("Opções", justify = "center")

    menu_relatorio.add_row(Align.left("[1] Relatório por categoria"))
    menu_relatorio.add_row(Align.left("[2] Relatório mensal"))
    menu_relatorio.add_row(Align.left("[bold #FF8C00][3] Voltar para o menu principal[/]"))

    console.print(menu_relatorio)


def mostrar_relatorio_mensal(relatorio, mes):
    """
    Exibe o relatório mensal.
    :param mes: Mês do relatório a ser exibido.
    :param relatorio: O relatório mensal a ser exibido.
    :return: None.
    """
    console = Console()
    menu = Table(title = f"Relatório Mensal: {converter_mes(mes)}", style = "#FF8C00")

    menu.add_column("Categoria", justify = "center")
    menu.add_column("Valor Total", justify = "center")

    total_salario = sum(r.valor for r in relatorio["receitas"]["salario"])
    menu.add_row("Salário", Align.left(f"[bold green]{formatar_valor(total_salario)}[/]"))

    total_renda_extra = sum(r.valor for r in relatorio["receitas"]["renda_extra"])
    menu.add_row("Renda Extra", Align.left(f"[bold green]{formatar_valor(total_renda_extra)}[/]"))

    total_freelance = sum(r.valor for r in relatorio["receitas"]["freelance"])
    menu.add_row("Freelance", Align.left(f"[bold green]{formatar_valor(total_freelance)}[/]"))

    menu.add_section()

    total_aluguel = sum(r.valor_gasto for r in relatorio["gastos_fixos"]["aluguel"])
    menu.add_row("Aluguel", Align.left(f"[bold red]{formatar_valor(total_aluguel)}[/]"))

    total_conta = sum(r.valor_gasto for r in relatorio["gastos_fixos"]["conta"])
    menu.add_row("Contas", Align.left(f"[bold red]{formatar_valor(total_conta)}[/]"))

    total_plano_saude = sum(r.valor_gasto for r in relatorio["gastos_fixos"]["plano_saude"])
    menu.add_row("Plano de Saúde", Align.left(f"[bold red]{formatar_valor(total_plano_saude)}[/]"))

    total_transporte = sum(r.valor_gasto for r in relatorio["gastos_fixos"]["transporte"])
    menu.add_row("Transporte", Align.left(f"[bold red]{formatar_valor(total_transporte)}[/]"))

    menu.add_section()

    total_alimentacao = sum(r.valor_gasto for r in relatorio["gastos_variaveis"]["alimentacao"])
    menu.add_row("Alimentação", Align.left(f"[bold red]{formatar_valor(total_alimentacao)}[/]"))

    total_lazer = sum(r.valor_gasto for r in relatorio["gastos_variaveis"]["lazer"])
    menu.add_row("Lazer", Align.left(f"[bold red]{formatar_valor(total_lazer)}[/]"))

    total_farmacia = sum(r.valor_gasto for r in relatorio["gastos_variaveis"]["farmacia"])
    menu.add_row("Farmácia", Align.left(f"[bold red]{formatar_valor(total_farmacia)}[/]"))

    total_diversos = sum(r.valor_gasto for r in relatorio["gastos_variaveis"]["diversos"])
    menu.add_row("Diversos", Align.left(f"[bold red]{formatar_valor(total_diversos)}[/]"))

    menu.add_section()

    total_investimentos = sum(r.valor_investido for r in relatorio["investimentos"])
    menu.add_row("Investimentos", Align.left(f"[bold cyan]{formatar_valor(total_investimentos)}[/]"))

    menu.add_section()

    total_ganho = total_salario + total_renda_extra + total_freelance
    menu.add_row("Total Ganho", Align.left(f"[bold green]{formatar_valor(total_ganho)}[/]"))

    total_gasto = (total_aluguel + total_conta + total_plano_saude + total_transporte + total_alimentacao + total_lazer
                   + total_farmacia + total_diversos)
    menu.add_row("Total Gasto", Align.left(f"[bold red]{formatar_valor(total_gasto)}[/]"))

    saldo_final = total_ganho - total_gasto
    if saldo_final >= 0:
        menu.add_row("Saldo", Align.left(f"[bold green]{formatar_valor(saldo_final)}[/]"))
    else:
        menu.add_row("Saldo", Align.left(f"[bold red]{formatar_valor(saldo_final)}[/]"))


    console.print(menu)
