from utils.services import conectar


def inserir_registro_investimento(registro):
    """
    Insere um novo registro de investimento no banco de dados.
    :param registro: Objeto do tipo Investimento.
    :return: None.
    """
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO investimentos (valor_investido, mes, tipo_investimento, entidade)
            VALUES (?, ?, ?, ?)
        """, (registro.valor_investido, registro.mes_investimento, registro.tipo_investimento,
                        registro.entidade))
        conexao.commit()