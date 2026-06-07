from rich import print as rprint

from fixed_expense.models import Aluguel, Conta, PlanoSaude, Transporte
from fixed_expense.repository import inserir_aluguel, inserir_conta, inserir_plano, inserir_transporte
from fixed_expense.ui import mostrar_menu_conta, mostrar_menu_gasto_fixo, mostrar_menu_plano, mostrar_menu_servicos
from shared.enums import TipoConta, TipoPlanoSaude, TipoTransporte
from utils.console import limpar_console
from utils.services import escolher_forma_pagamento
from utils.validators import validar_float, validar_integer, validar_mes


def escolher_tipo_gasto_fixo():
    """
    Exibe o menu de gastos fixos e direciona para o registro da categoria escolhida.
    :return: None.
    """
    while True:
        limpar_console()
        mostrar_menu_gasto_fixo()
        indice = validar_integer("Escolha uma opção: ")
        match indice:
            case 1:
                registrar_aluguel()
            case 2:
                registrar_conta()
            case 3:
                registrar_plano_saude()
            case 4:
                registrar_transporte()
            case 5:
                limpar_console()
                break
            case _:
                rprint("[bold red]Insira um comando válido![/]")


def registrar_aluguel():
    """
    Registra um aluguel no banco de dados.
    :return: None
    """
    limpar_console()
    valor = validar_float("Valor do aluguel: R$ ")
    mes = validar_mes("Mês: ")
    proprietario = input("Nome do proprietário: ")
    forma_pagamento = escolher_forma_pagamento()
    endereco = input("Endereço do imóvel: ").strip()
    numero = input("Número do imóvel: ").strip()
    novo_registro = Aluguel(valor, mes, proprietario, forma_pagamento, endereco, numero)
    inserir_aluguel(novo_registro)


def registrar_conta():
    """
    Registra uma conta no banco de dados.
    :return: None
    """
    limpar_console()
    valor = validar_float("Valor da conta: R$ ")
    mes = validar_mes("Mês: ")
    empresa = input("Nome da empresa: ").strip().title()
    forma_pagamento = escolher_forma_pagamento()
    tipo_conta = escolher_tipo_conta()
    novo_registro = Conta(valor, mes, empresa, forma_pagamento, tipo_conta)
    inserir_conta(novo_registro)


def registrar_plano_saude():
    """
    Registra um plano de saúde no banco de dados.
    :return: None
    """
    limpar_console()
    valor = validar_float("Valor do Plano: R$ ")
    mes = validar_mes("Mês: ")
    empresa = input("Nome da operadora: ").strip().title()
    forma_pagamento = escolher_forma_pagamento()
    tipo_plano = escolher_tipo_plano()
    novo_registro = PlanoSaude(valor, mes, empresa, forma_pagamento, tipo_plano)
    inserir_plano(novo_registro)


def registrar_transporte():
    """
    Registra um serviço de transporte no banco de dados.
    :return: None
    """
    limpar_console()
    valor = validar_float("Valor gasto: R$ ")
    mes = validar_mes("Mês: ")
    empresa = input("Local ou empresa: ").strip().title()
    forma_pagamento = escolher_forma_pagamento()
    tipo_servico = escolher_tipo_servico()
    novo_registro = Transporte(valor, mes, empresa, forma_pagamento, tipo_servico)
    inserir_transporte(novo_registro)


def escolher_tipo_conta():
    """
    Exibe o menu de tipos de conta e retorna a opção escolhida pelo usuário.
    :return: Tipo de conta selecionado (str).
    """
    mostrar_menu_conta()
    while True:
        opcao = validar_integer("Escolha o tipo de conta: ")
        match opcao:
            case 1:
                return TipoConta.AGUA.value
            case 2:
                return TipoConta.LUZ.value
            case 3:
                return TipoConta.INTERNET.value
            case 4:
                return TipoConta.OUTROS.value
            case _:
                rprint("[bold red]Insira um comando válido![/]")


def escolher_tipo_plano():
    """
    Exibe o menu de tipos de plano de saúde e retorna a opção escolhida pelo usuário.
    :return: Tipo de plano de saúde selecionado (str).
    """
    mostrar_menu_plano()
    while True:
        opcao = validar_integer("Escolha o tipo de plano: ")
        match opcao:
            case 1:
                return TipoPlanoSaude.INDIVIDUAL.value
            case 2:
                return TipoPlanoSaude.FAMILIAR.value
            case 3:
                return TipoPlanoSaude.EMPRESARIAL.value
            case 4:
                return TipoPlanoSaude.OUTROS.value
            case _:
                rprint("[bold red]Insira um comando válido![/]")


def escolher_tipo_servico():
    """
    Exibe o menu de tipos de serviço de transporte e retorna a opção escolhida pelo usuário.
    :return: Tipo de serviço de transporte selecionado (str).
    """
    mostrar_menu_servicos()
    while True:
        opcao = validar_integer("Escolha o tipo de serviço: ")
        match opcao:
            case 1:
                return TipoTransporte.COMBUSTIVEL.value
            case 2:
                return TipoTransporte.MANUTENCAO.value
            case 3:
                return TipoTransporte.TRANSPORTE_PUBLICO.value
            case 4:
                return TipoTransporte.OUTROS.value
            case _:
                rprint("[bold red]Insira um comando válido![/]")