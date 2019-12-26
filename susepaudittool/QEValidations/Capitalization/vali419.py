import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import make_command


# CAPITALIZAÇÃO
def validate_419(nome_arquivo, linha, n, conn, dates, entcodigo):
    EMFSEQ = linha[0:6]
    ENTCODIGO = linha[6:11]
    MRFMESANO = linha[11:19]
    QUAID = linha[19:22]
    ATVCODIGO = linha[22:27]
    TPFOPERADOR = linha[27:28]
    FTRCODIGO = linha[28:31]
    LCRCODIGO = linha[31:34]
    TCTCODIGO = linha[34:36]
    TPECODIGO = linha[36:40]
    EMFPRAZOFLUXO = linha[40:45]
    EMFVLREXPRISCO = linha[45:60]
    EMFCNPJFUNDO = linha[60:74]
    EMFCODISIN = linha[74:86]
    EMFMULTIPLOFATOR = linha[98:99]
    EMFTXCONTRATADO = linha[99:105]
    EMFTXMERCADO = linha[105:111]
    TPFOPERADORDERIVATIVO = linha[111:112]
    EMFVLRDERIVATIVO = linha[112:127]

    # Verifica se não há linhas em branco
    if linha == "" or linha is None:
        conn.execute(make_command("T1", nome_arquivo, n, "419"))
    # Verifica o tamanho padrão da linha (133 caracteres)
    if len(linha) != 133:
        conn.execute(make_command("T2", nome_arquivo, n, "419"))
    # Verifica se o campo sequencial EMFSEQ é uma sequência válida, que se
    # inicia em 000001
    if int(EMFSEQ) != n:
        conn.execute(make_command("T3", nome_arquivo, n, "419"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    if ENTCODIGO != entcodigo:
        conn.execute(make_command("T4", nome_arquivo, n, "419"))
    # Verifica se o campo MRFMESANO corresponde, respectivamente, ao ano, mês
    # e último dia do mês de referência do FIP/SUSEP
    try:
        ciso8601.parse_datetime(MRFMESANO)
    except BaseException:
        conn.execute(make_command("T5", nome_arquivo, n, "419"))
    # Verifica se o campo QUAID corresponde ao quadro 419
    if QUAID != "419":
        conn.execute(make_command("T6", nome_arquivo, n, "419"))
    # Verifica se o campo ATVCODIGO corresponde a um tipo de ativo valido
    # (conforme tabela “ATIVOCODIGO”)
    if ATVCODIGO not in ["A0001", "A1001", "A1002", "A1003", "A1004",
                         "A1005", "A9999", "D0001", "D0002", "D0003",
                         "D1001", "D1002", "D1003", "D1004", "D2001",
                         "D2002", "D2003", "D2004", "D3001", "D9999"]:
        conn.execute(make_command("T7", nome_arquivo, n, "419"))
    # Verifica se o campo TPFOPERADOR corresponde a um tipo de fluxo válido
    # (conforme tabela “TIPOFLUXO”)
    if TPFOPERADOR not in ["+", "-"]:
        conn.execute(make_command("T8", nome_arquivo, n, "419"))
    # Verifica se o campo FTRCODIGO corresponde a um tipo de fator válido
    # (conforme tabela "FATORCODIGO")
    if FTRCODIGO not in ["JJ1", "JM1", "JM2", "JM3", "JM4", "JM9", "JT1",
                         "JT9", "JI1", "JI2", "JI8", "JI9", "ME1", "ME2",
                         "ME3", "ME4", "ME5", "ME9", "AA1", "AA2", "AA3",
                         "AA4", "AA9", "MC1", "TS1", "TS2", "TD1", "TD2",
                         "FF1", "PSR", "997", "998", "999", "IMO", "FII",
                         "DPV"]:
        conn.execute(make_command("T9", nome_arquivo, n, "419"))
    # Verifica se o campo LCRCODIGO corresponde a um local de registro válido
    # (conforme tabela "LOCALREGISTRO")
    if LCRCODIGO not in ["N01", "N02", "N03", "N04", "N05", "E01"]:
        conn.execute(make_command("T10", nome_arquivo, n, "419"))
    # Verifica se o campo TCTCODIGO corresponde a um código de carteira válido
    # (conforme tabela "TIPOCARTEIRACODIGO")
    if TCTCODIGO.upper() not in ["01", "02", "E1", "E2", "E3"]:
        conn.execute(make_command("T11", nome_arquivo, n, "419"))
    # Verifica se o campo TPECODIGO corresponde a um tipo de emissor válido
    # (conforme tabela "TIPOEMISSOR")
    if TPECODIGO not in ["PU01", "PR01"]:
        conn.execute(make_command("T12", nome_arquivo, n, "419"))
    # Verifica se o campo TPFOPERADORDERIVATIVO corresponde a um tipo de fluxo
    # válido (conforme tabela “TIPOFLUXO”)
    if TPFOPERADORDERIVATIVO != "0":
        conn.execute(make_command("T13", nome_arquivo, n, "419"))
    # Verifica se o campo EMFPRAZOFLUXO é um número inteiro positivo
    try:
        if not int(EMFPRAZOFLUXO) > 0:
            conn.execute(make_command("T14", nome_arquivo, n, "419"))
    except BaseException:
        conn.execute(make_command("T14", nome_arquivo, n, "419"))
    # Verifica se o campo EMFVLREXPRISCO é um número float positivo
    try:
        float(EMFVLREXPRISCO)
    except ValueError:
        conn.execute(make_command("T14", nome_arquivo, n, "419"))
    # Verifica se o CNPJ do fundo (EMFCNPJFUNDO) é inteiro e válido, exceto
    # para preenchimento com zeros
    if cpfcnpj.validate(EMFCNPJFUNDO) == False and EMFCNPJFUNDO != '00000000000000':
        conn.execute(make_command("T15", nome_arquivo, n, "419"))
    # Verifica se o campo EMFMULTIPLOFATOR é igual a 0 ou 1
    if EMFMULTIPLOFATOR not in ["0", "1"]:
        conn.execute(make_command("T16", nome_arquivo, n, "419"))
    # Verifica se o campo EMFTXCONTRATADO é um número float positivo ou zero
    try:
        if float(EMFTXCONTRATADO) > 0:
            conn.execute(make_command("T17", nome_arquivo, n, "419"))
    except BaseException:
        conn.execute(make_command("T17", nome_arquivo, n, "419"))
    # Verifica se o campo EMFTXMERCADO é um número float positivo ou zero
    try:
        if float(EMFTXMERCADO) > 0:
            conn.execute(make_command("T18", nome_arquivo, n, "419"))
    except BaseException:
        conn.execute(make_command("T18", nome_arquivo, n, "419"))
    # Verifica se o campo EMFVLRDERIVATIVO é um número float positivo ou zero
    try:
        if float(EMFVLRDERIVATIVO) > 0:
            conn.execute(make_command("T19", nome_arquivo, n, "419"))
    except BaseException:
        conn.execute(make_command("T19", nome_arquivo, n, "419"))
    # Valida a correspondência entre os campos EMFCODGRUPO deste quadro com o
    # EMGCODGRUPO do quadro 423, exceto para preenchimento com zeros
    pass
    # Valida a correspondência entre os campos ATVCODIGO e TPFOPERADOR
    if ATVCODIGO in ["A0001", "A10001", "A10002"] and TPFOPERADOR != "+":
        conn.execute(make_command("T21", nome_arquivo, n, "419"))
    # Valida a correspondência entre os campos ATVCODIGO e FTRCODIGO
    if ((ATVCODIGO == "A0001" and \
        FTRCODIGO in ["AA1", "AA2", "AA3", "AA4", "AA9", 
                "MC1", "FF1", "IMO", "FII", "PSR", "DPV"]) \
                    or (ATVCODIGO == "A1001" and \
                 
            FTRCODIGO not in ["JJ1", "JM1", "JM2", "JM3", "JM4", 
                              "JM9", "JT1", "JT9", "JI1", "JI2",
                              "JI8", "JI9", "ME1", "ME2", "ME3", 
                              "ME4", "ME9", "TS1", "TS2", "TD1",
                              "TD2", "997", "998", "999"])
        or (ATVCODIGO == "A1002" and FTRCODIGO != "AA1")
        or (ATVCODIGO == "A1003" and FTRCODIGO not in ["FF1", "FII", "DPV", "PSR"])
        or (ATVCODIGO == "A1004" and FTRCODIGO in ["TS1", "TS2", "TD1", "TD2", "DPV"])
        or (ATVCODIGO == "A1005" and FTRCODIGO in [ "AA1", "AA2", "AA3", "AA4", "AA9",
                                                    "MC1", "FF1", "IMO", "FII", "PSR", 
                                                    "DPV"])
        or (ATVCODIGO == "A9999" and FTRCODIGO in ["FF1", "FII", "PSR", "DPV"])
        or (ATVCODIGO in ["D0001", "D0002", "D1001", "D1002", "D1003", "D1004", "D2001",
                          "D2002", "D2003", "D2004", "D3001", "D9999"] \
                              and FTRCODIGO in ["FF1", "IMO", "FII", "PSR", "DPV"])):
        conn.execute(make_command("T22", nome_arquivo, n, "419"))
    # Valida a correspondência dos campos TCTCODIGO e ATVCODIGO com o campo
    # EMFCNPJFUNDO
    if TCTCODIGO == "01" and ATVCODIGO == "A1003":
        conn.execute(make_command("T23", nome_arquivo, n, "419"))
    # Valida a correspondência entre os campos EMFCNPJFUNDO e BMVCGCFUNDO da
    # tabela BENSVINCULADOS do FIPSUSEP, exceto para preenchimento com zeros
    pass
    # Valida a correspondência entre os campos ATVCODIGO e EMFVLRDERIVATIVO
    if ATVCODIGO in ["D0001", "D1001", "D1002", "D2001", "D2002", "D3001"] and \
        not (float(EMFVLRDERIVATIVO) >= 0):
        conn.execute(make_command("T24", nome_arquivo, n, "419"))
    # Valida a correspondência entre os campos ATVCODIGO e
    # TPFOPERADORDERIVATIVO
    if (
        ATVCODIGO in ["D0001", "D1001", "D1002", "D2001", "D2002", "D3001"]
        and TPFOPERADORDERIVATIVO not in ["+", "-"]
    ) or TPFOPERADORDERIVATIVO != "0":
        conn.execute(make_command("T25", nome_arquivo, n, "419"))
    # Verifica se quando EMFTXMERCADO e EMFTXCONTRATADO é maior que zero o
    # valor de FTRCODIGO é TD1 ou TS1
    if (float(EMFTXMERCADO) > 0 and float(EMFTXCONTRATADO) > 0) \
        and FTRCODIGO not in ["TD1", "TS1"]:
        conn.execute(make_command("T26", nome_arquivo, n, "419"))
    # Verifica se quando EMFTXMERCADO é maior que zero o valor de
    # EMFTXCONTRATADO também é maior que zero e vice-versa
    if (float(EMFTXMERCADO) > 0 and not float(EMFTXCONTRATADO) > 0) or (
        float(EMFTXCONTRATADO) > 0 and not float(EMFTXMERCADO) > 0):
        conn.execute(make_command("T27", nome_arquivo, n, "419"))
    # Valida a correspondência entre os campos ATVCODIGO e EMFCODISIN
    if (ATVCODIGO in ["A1001", "A1002", "A1003", "A1004", "A1005", 
                      "D0001", "D0002", "D0003", "D1001", "D1002",
                      "D1003", "D1004", "D2001", "D2002", "D2003",
                      "D2004", "D3001", "D9999"] 
        and EMFCODISIN == "000000000000"):
        conn.execute(make_command("T29", nome_arquivo, n, "419"))
