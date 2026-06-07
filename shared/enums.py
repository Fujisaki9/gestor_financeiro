from enum import Enum


class TipoAlimentacao(Enum):
    SUPERMERCADO = "Supermercado"
    RESTAURANTE = "Restaurante"
    DELIVERY = "Delivery"
    OUTROS = "Outros"


class TipoLazer(Enum):
    SHOPPING = "Shopping"
    VIAGEM = "Viagem"
    ACADEMIA = "Academia"
    OUTROS = "Outros"


class TipoFarmacia(Enum):
    MEDICAMENTO = "Medicamento"
    COSMETICO = "Cosmético"
    SUPLEMENTO = "Suplemento"
    OUTROS = "Outros"


class TipoTransporte(Enum):
    COMBUSTIVEL = "Combustível"
    MANUTENCAO = "Manutenção"
    TRANSPORTE_PUBLICO = "Transporte Público"
    OUTROS = "Outros"


class TipoPlanoSaude(Enum):
    INDIVIDUAL = "Individual"
    FAMILIAR = "Familiar"
    EMPRESARIAL = "Empresarial"
    OUTROS = "Outros"


class TipoConta(Enum):
    AGUA = "Água"
    LUZ = "Luz"
    INTERNET = "Internet"
    OUTROS = "Outros"


class TipoInvestimento(Enum):
    POUPANCA = "Poupança"
    RESERVA = "Reserva de Emergência"
    ACOES = "Ações"
    OUTROS = "Outros"


class TipoPagamento(Enum):
    DINHEIRO = "Dinheiro"
    PIX = "PIX"
    BOLETO = "Boleto"
    CARTAO = "Cartão"
    OUTROS = "Outros"
