import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import *

moedas = get_moedas()


# RESEGUROS
def validate_406(nome_arquivo, linha, n, conn, dates,
                 entcodigo, gracodigos):
    # Verifica se não há linhas em branco
    if linha == "" or linha is None:
        conn.execute(make_command("T1", nome_arquivo, n, "406"))
    # Verifica o tamanho padrão da linha (deve conter 130 caracteres)
    if len(linha) != 130:
        conn.execute(make_command("T2", nome_arquivo, n, "406"))
    # Verifica se o campo sequencial SLASEQ é uma sequência válida, que se
    # inicia em 0000001
    if int(linha[0:7]) != n:
        conn.execute(make_command("T3", nome_arquivo, n, "406"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    if linha[7:12] != entcodigo:
        conn.execute(make_command("T4", nome_arquivo, n, "406"))
    # Verifica se o campo MRFMESANO corresponde a um ano e mês válidos
    try:
        ciso8601.parse_datetime(linha[12:18] + "01")
    except ValueError:
        conn.execute(make_command("T5", nome_arquivo, n, "406"))
    # Verifica se o campo GRACODIGO corresponde a um grupo de ramos válido
    # operado pelo ressegurador
    if linha[18:20] not in gracodigos:
        conn.execute(make_command("T6", nome_arquivo, n, "406"))
    # Verifica se o campo SLATIPOPERA foi preenchido com um tipo de operação
    # válido
    if linha[20] not in ["1", "2"]:
        conn.execute(make_command("T7", nome_arquivo, n, "406"))
    # Verifica se o campo SLATIPOCONT foi preenchido com um tipo de contrato
    # válido
    if linha[67] not in ["1", "2"]:
        conn.execute(make_command("T8", nome_arquivo, n, "406"))
    # Verifica se o campo SLACODCESS corresponde a um código de sociedade
    # válido ou ‘99999’ e valida a correspondência entre os campos SLATIPOPERA
    # e SLACODCESS
    if (linha[20:21] == "1" and int(linha[68:73]) not in [i for i in range(1, 20000)]) or (
            linha[20:21] == "2" and int(linha[68:73]) not in [i for i in range(30000, 60000)]):
        conn.execute(make_command("T9", nome_arquivo, n, "406"))
    # Verifica se os campos SLADATAOCORR, SLADATACOMUNICA e SLADATAREG
    # correspondem a uma data válida. Nos casos em que a modalidade do
    # contrato seja 'Proporcional: Cota Parte' ou 'Proporcional: ER', os
    # campos podem ser preenchidos com '99999999'
    try:
        ciso8601.parse_datetime(linha[73:81])
        ciso8601.parse_datetime(linha[81:89])
        ciso8601.parse_datetime(linha[89:97])
    except ValueError:
        if (linha[124:126] in ["1", "2"]) and (linha[73:81] ==
                                               "99999999" and linha[81:89] == "99999999" and linha[89:97] == "99999999"):
            conn.execute(make_command("T10", nome_arquivo, n, "406"))
    # Verifica se o valor dos campos SLAVALORMOVPEN e SLAVALORMOVTOT é float
    try:
        float(linha[97:110].replace(",", "."))
        float(linha[110:123].replace(",", "."))
    except ValueError:
        conn.execute(make_command("T11", nome_arquivo, n, "406"))
    # Verifica se o campo SLATIPOSIN foi preenchido com um tipo de sinistro
    # válido
    if linha[123] not in ["1", "2"]:
        conn.execute(make_command("T12", nome_arquivo, n, "406"))
    # Verifica se o campo SLAMODCONT foi preenchido com uma modalidade de
    # contrato válida, exceto nos casos em que o tipo de contrato seja
    # ‘Facultativo’, quando o campo deve ser preenchido com ‘99
    if linha[124:126] not in ["01", "02", "03", "04", "05", "06"] and (
            linha[67] == "2" and linha[124:126] != "99"):
        conn.execute(make_command("T13", nome_arquivo, n, "406"))
    # Verifica se o campo SLAMOEDA foi preenchido com uma moeda válida
    if linha[126:129] not in moedas:
        conn.execute(make_command("T14", nome_arquivo, n, "406"))
    # Verifica se o campo SLABASEIND foi preenchido com uma base indenitária
    # válida
    if linha[129] not in ["1", "2", "3"]:
        conn.execute(make_command("T15", nome_arquivo, n, "406"))