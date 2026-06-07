def converter_mes(mes) -> str:
    """
    Converte o número de um mês para seu nome por extenso.
    :param mes: Número do mês (1-12).
    :return: Nome do mês.
    """
    meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    return meses[mes]


def formatar_valor(valor) -> str:
    """
    Formata um valor numérico para o formato monetário brasileiro (R$ 1.234,56).
    :param valor: Valor numérico a ser formatado.
    :return: Valor formatado.
    """
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")