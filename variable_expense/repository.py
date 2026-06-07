from utils.services import conectar


def inserir_registro_alimentacao(registro):
    """
    Insere um registro de alimentação no banco de dados.
    :param registro: Objeto do tipo Alimentacao.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO alimentacao (valor, mes, local, forma_pagamento, tipo_servico)
            VALUES (?, ?, ?, ?, ?)
        """, (registro.valor_gasto, registro.mes, registro.origem, registro.forma_pagamento,
                        registro.tipo_alimentacao))
        conexao.commit()


def inserir_registro_lazer(registro):
    """
    Insere um registro de lazer no banco de dados.
    :param registro: Objeto do tipo Lazer.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO lazer (valor, mes, local, forma_pagamento, tipo_servico)
            VALUES (?, ?, ?, ?, ?)
        """, (registro.valor_gasto, registro.mes, registro.origem, registro.forma_pagamento,
                        registro.tipo_lazer))
        conexao.commit()


def inserir_registro_farmacia(registro):
    """
    Insere um registro de farmácia no banco de dados.
    :param registro: Objeto do tipo Farmacia.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO farmacia (valor, mes, local, forma_pagamento, tipo_servico)
            VALUES (?, ?, ?, ?, ?)
        """, (registro.valor_gasto, registro.mes, registro.origem, registro.forma_pagamento,
                        registro.tipo_farmacia))
        conexao.commit()


def inserir_registro_diverso(registro):
    """
    Insere um registro de gasto diverso no banco de dados.
    :param registro: Objeto do tipo Diversos.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO diversos (valor, mes, local, forma_pagamento, tipo_servico)
            VALUES (?, ?, ?, ?, ?)
        """, (registro.valor_gasto, registro.mes, registro.origem, registro.forma_pagamento,
                        registro.descricao_gasto))
        conexao.commit()