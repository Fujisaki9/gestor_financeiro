from rich.console import Console
from rich import print as rprint

from report.repository import (buscar_salario, buscar_renda_extra, buscar_freelance, buscar_aluguel, buscar_conta,
                                  buscar_plano_saude, buscar_transporte, buscar_alimentacao, buscar_lazer,
                                  buscar_farmacia, buscar_diversos, buscar_investimentos, buscar_salario_mes,
                                  buscar_renda_extra_mes, buscar_freelance_mes, buscar_aluguel_mes, buscar_conta_mes,
                                  buscar_plano_saude_mes, buscar_transporte_mes, buscar_alimentacao_mes,
                                  buscar_lazer_mes, buscar_farmacia_mes, buscar_diversos_mes, buscar_investimentos_mes)
from report.ui import (mostrar_menu_relatorio, mostrar_relatorio_salario, mostrar_relatorio_renda_extra,
                          mostrar_relatorio_freelance, mostrar_relatorio_aluguel, mostrar_relatorio_conta,
                          mostrar_relatorio_plano_saude, mostrar_relatorio_transporte, mostrar_relatorio_alimentacao,
                          mostrar_relatorio_lazer, mostrar_relatorio_farmacia, mostrar_relatorio_diversos,
                          mostrar_relatorio_investimento, mostrar_opcao_relatorio, mostrar_relatorio_mensal)
from utils.console import limpar_console
from utils.validators import validar_integer, validar_mes


def escolher_tipo_relatorio():
    """
    Exibe o menu de relatórios e permite ao usuário escolher qual relatório deseja visualizar.
    :return: None.
    """
    console = Console()
    while True:
        limpar_console()
        mostrar_menu_relatorio()
        opcao = validar_integer("Escolha uma opção: ")
        match opcao:
            case 1:
                mostrar_relatorio_salario(buscar_salario())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 2:
                mostrar_relatorio_renda_extra(buscar_renda_extra())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 3:
                mostrar_relatorio_freelance(buscar_freelance())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 4:
                mostrar_relatorio_aluguel(buscar_aluguel())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 5:
                mostrar_relatorio_conta(buscar_conta())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 6:
                mostrar_relatorio_plano_saude(buscar_plano_saude())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 7:
                mostrar_relatorio_transporte(buscar_transporte())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 8:
                mostrar_relatorio_alimentacao(buscar_alimentacao())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 9:
                mostrar_relatorio_lazer(buscar_lazer())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 10:
                mostrar_relatorio_farmacia(buscar_farmacia())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 11:
                mostrar_relatorio_diversos(buscar_diversos())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 12:
                mostrar_relatorio_investimento(buscar_investimentos())
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 13:
                limpar_console()
                break
            case _:
                rprint("ERRO: Insira um comando válido!")


def montar_relatorio_mensal(mes):
    """
    Monta um relatório mensal com base nos dados do mês especificado.
    :param mes: O mês para o qual o relatório deve ser montado.
    :return: Um dicionário contendo os dados do relatório mensal.
    """
    relatorio = {
        "receitas": {
            "salario": buscar_salario_mes(mes),
            "renda_extra": buscar_renda_extra_mes(mes),
            "freelance": buscar_freelance_mes(mes)
        },
        "gastos_fixos": {
            "aluguel": buscar_aluguel_mes(mes),
            "conta": buscar_conta_mes(mes),
            "plano_saude": buscar_plano_saude_mes(mes),
            "transporte": buscar_transporte_mes(mes)
        },
        "gastos_variaveis": {
            "alimentacao": buscar_alimentacao_mes(mes),
            "lazer": buscar_lazer_mes(mes),
            "farmacia": buscar_farmacia_mes(mes),
            "diversos": buscar_diversos_mes(mes),
        },
        "investimentos": buscar_investimentos_mes(mes)
    }
    return relatorio


def abrir_menu_relatorio():
    """
    Abre o menu de relatórios.
    :return: None.
    """
    console = Console()
    while True:
        limpar_console()
        mostrar_opcao_relatorio()
        opcao = validar_integer("Escolha uma opção: ")
        match opcao:
            case 1:
                escolher_tipo_relatorio()
            case 2:
                mes = validar_mes("Digite o mês para o qual deseja gerar o relatório (1-12): ")
                relatorio_mensal = montar_relatorio_mensal(mes)
                limpar_console()
                mostrar_relatorio_mensal(relatorio_mensal, mes)
                console.input("[bold #FF8C00]Pressione ENTER para voltar ao menu.[/]")
            case 3:
                break
            case _:
                rprint("ERRO: Insira um comando válido!")