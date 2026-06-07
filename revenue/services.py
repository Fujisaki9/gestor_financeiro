from rich import print as rprint

from revenue.models import Salario, RendaExtra, Freelance
from revenue.repository import inserir_freelance, inserir_renda_extra, inserir_salario
from revenue.ui import mostrar_menu_receita
from utils.console import limpar_console
from utils.validators import validar_float, validar_integer, validar_mes


def escolher_tipo_receita():
    """
    Exibe o menu de receitas e direciona para o registro da categoria escolhida.
    :return: None.
    """
    while True:
        limpar_console()
        mostrar_menu_receita()
        indice = validar_integer("Escolha uma opção: ")
        match indice:
            case 1:
                registrar_salario()
            case 2:
                registrar_renda_extra()
            case 3:
                registrar_freelance()
            case 4:
                limpar_console()
                break
            case _:
                rprint("[bold red]Insira um comando válido![/]")


def registrar_salario():
    """
    Registra um novo registro de salário no banco de dados.
    :return: None.
    """
    limpar_console()
    salario = validar_float("Salário: R$ ")
    mes = validar_mes("Mês: ")
    empresa = input("Nome da empresa: ").strip().title()
    cargo = input("Cargo ocupado: ").strip().title()
    novo_registro = Salario(salario, mes, empresa, cargo)
    inserir_salario(novo_registro)


def registrar_renda_extra():
    """
    Registra um novo registro de renda extra no banco de dados.
    :return: None.
    """
    limpar_console()
    valor = validar_float("Renda obtida: R$ ")
    mes = validar_mes("Mês: ")
    atividade = input("Atividade realizada: ").strip().title()
    custo = validar_float("Investimento realizado: R$ ")
    novo_registro = RendaExtra(valor, mes, atividade, custo)
    inserir_renda_extra(novo_registro)


def registrar_freelance():
    """
    Registra um novo registro de freelance no banco de dados.
    :return: None
    """
    limpar_console()
    preco_hora = validar_float("Preço/Hora: R$ ")
    horas_trabalhadas = validar_integer("Horas trabalhadas: ")
    mes = validar_mes("Mês: ")
    contratante = input("Nome do contratante: ").strip().title()
    novo_registro = Freelance(mes, contratante, preco_hora, horas_trabalhadas)
    inserir_freelance(novo_registro)