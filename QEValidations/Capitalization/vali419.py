import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import make_command



# CAPITALIZAÇÃO
def validate_419(nome_arquivo, linha, n, conn, dates,
                 entcodigo, ramcodigos, esrcodcess):
    # Verifica se não há linhas em branco
    # Verifica o tamanho padrão da linha (133 caracteres)
    if linha == "" or linha is None:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo sequencial EMFSEQ é uma sequência válida, que se
    # inicia em 000001
    if len(linha) != n:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    if linha[6:11] != entcodigo:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo MRFMESANO corresponde, respectivamente, ao ano, mês
    # e último dia do mês de referência do FIP/SUSEP
    try:
        ciso8601.parse_datetime(linha[11:20])
    except BaseException:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo QUAID corresponde ao quadro 419
    if linha[19:22] != "419":
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo ATVCODIGO corresponde a um tipo de ativo valido
    # (conforme tabela “ATIVOCODIGO”)
    if linha[22:27] not in ["A0001", "A1001", "A1002", "A1003", "A1004",
                            "A1005", "A9999", "D0001", "D0002", "D0003",
                            "D1001", "D1002", "D1003", "D1004", "D2001",
                            "D2002", "D2003", "D2004", "D3001", "D9999"]:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo TPFOPERADOR corresponde a um tipo de fluxo válido
    # (conforme tabela “TIPOFLUXO”)
    if linha[27] not in ["+", "-"]:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo FTRCODIGO corresponde a um tipo de fator válido
    # (conforme tabela "FATORCODIGO")
    if linha[28:31] not in ["JJ1", "JM1", "JM2", "JM3", "JM4", "JM9", "JT1",
                            "JT9", "JI1", "JI2", "JI8", "JI9", "ME1", "ME2",
                            "ME3", "ME4", "ME5", "ME9", "AA1", "AA2", "AA3",
                            "AA4", "AA9", "MC1", "TS1", "TS2", "TD1", "TD2",
                            "FF1", "PSR", "997", "998", "999", "IMO", "FII",
                            "DPV"]:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo LCRCODIGO corresponde a um local de registro válido
    # (conforme tabela "LOCALREGISTRO")
    if linha[31:34] not in ["N01", "N02", "N03", "N04", "N05", "E01"]:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo TCTCODIGO corresponde a um código de carteira válido
    # (conforme tabela "TIPOCARTEIRACODIGO")
    if linha[34:36].upper() not in ["01", "02", "E1", "E2", "E3"]:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo TPECODIGO corresponde a um tipo de emissor válido
    # (conforme tabela "TIPOEMISSOR")
    if linha[36:40] not in ["PU01", "PR01"]:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo TPFOPERADORDERIVATIVO corresponde a um tipo de fluxo
    # válido (conforme tabela “TIPOFLUXO”)
    if linha[111] not in ["+", "-"]:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo EMFPRAZOFLUXO é um número inteiro positivo
    try:
        if not int(linha[40:45]) > 0:
            conn.execute(make_command("T1", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo EMFVLREXPRISCO é um número float positivo
    try:
        float(linha[45:60])
    except ValueError:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o CNPJ do fundo (EMFCNPJFUNDO) é inteiro e válido, exceto
    # para preenchimento com zeros
    if int(linha[60:74]) != 0 and cpfcnpj.validate(linha[60:75]) == False:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo EMFMULTIPLOFATOR é igual a 0 ou 1
    if linha[98] not in ["0", "1"]:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo EMFTXCONTRATADO é um número float positivo ou zero
    try:
        if not float(linha[99:105]) > 0:
            conn.execute(make_command("T1", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo EMFTXMERCADO é um número float positivo ou zero
    try:
        if not float(linha[105:111]) > 0:
            conn.execute(make_command("T1", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Verifica se o campo EMFVLRDERIVATIVO é um número float positivo ou zero
    try:
        if not float(linha[112:127]) > 0:
            conn.execute(make_command("T1", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Valida a correspondência entre os campos EMFCODGRUPO deste quadro com o
    # EMGCODGRUPO do quadro 423, exceto para preenchimento com zeros
    pass
    # Valida a correspondência entre os campos ATVCODIGO e TPFOPERADOR
    if (linha[22:27] in ["A0001", "A10001", "A10002"] and linha[27] != "+"):
        conn.execute(make_command("T1", nome_arquivo, n, "376"))
    # Valida a correspondência entre os campos ATVCODIGO e FTRCODIGO
    pass
    # Valida a correspondência dos campos TCTCODIGO e ATVCODIGO com o campo
    # EMFCNPJFUNDO
    pass
    # Valida a correspondência entre os campos EMFCNPJFUNDO e BMVCGCFUNDO da
    # tabela BENSVINCULADOS do FIPSUSEP, exceto para preenchimento com zeros
    pass
    # Valida a correspondência entre os campos ATVCODIGO e EMFVLRDERIVATIVO
    pass
    # Valida a correspondência entre os campos ATVCODIGO e
    # TPFOPERADORDERIVATIVO
    pass
    # Verifica se quando EMFTXMERCADO e EMFTXCONTRATADO é maior que zero o
    # valor de FTRCODIGO é TD1 ou TS1
    pass
    # Verifica se quando EMFTXMERCADO é maior que zero o valor de
    # EMFTXCONTRATADO também é maior que zero e vice-versa
    pass
    # Valida a correspondência entre os campos ATVCODIGO e EMFCODISIN
    pass