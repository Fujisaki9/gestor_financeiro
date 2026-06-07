from utils.services import conectar


def inserir_aluguel(aluguel):
    """
    Insere um aluguel no banco de dados.
    :param aluguel: Objeto do tipo Aluguel.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO aluguel (valor, mes, proprietario, forma_pagamento, endereco_imovel, numero_imovel)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (aluguel.valor_gasto, aluguel.mes, aluguel.origem, aluguel.forma_pagamento,
                        aluguel.endereco_imovel, aluguel.numero_imovel))
        conexao.commit()


def inserir_conta(conta):
    """
    Insere uma conta no banco de dados.
    :param conta: Objeto do tipo Conta.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO conta (valor, mes, empresa, forma_pagamento, tipo_conta)
            VALUES (?, ?, ?, ?, ?)
        """,(conta.valor_gasto, conta.mes, conta.origem, conta.forma_pagamento, conta.tipo_conta))
        conexao.commit()


def inserir_plano(plano):
    """
    Insere um plano de saúde no banco de dados.
    :param plano: Objeto do tipo PlanoSaude.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO plano_saude (valor, mes, operadora, forma_pagamento, tipo_plano)
            VALUES (?, ?, ?, ?, ?)
        """,(plano.valor_gasto, plano.mes, plano.origem, plano.forma_pagamento, plano.tipo_plano))
        conexao.commit()


def inserir_transporte(servico):
    """
    Insere um serviço de transporte no banco de dados.
    :param servico: Objeto do tipo Transporte.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO transporte (valor, mes, empresa,  forma_pagamento, tipo_servico)
            VALUES (?, ?, ?, ?, ?)
        """,(servico.valor_gasto, servico.mes, servico.origem, servico.forma_pagamento, servico.tipo_servico))
        conexao.commit()
