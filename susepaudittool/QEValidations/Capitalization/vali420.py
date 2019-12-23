import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import make_command


# CAPITALIZAÇÃO
def validate_420(nome_arquivo, linha, n, conn, dates,
                 entcodigo):
    EMCSEQ = linha[0:6]
    ENTCODIGO = linha[6:11]
    MRFMESANO = linha[11:19]
    QUAID = linha[19:22]
    DOCCODIGO = linha[22:27]
    TPFOPERADOR = linha[27:28]
    FTRCODIGO = linha[28:31]
    EMCPRAZOFLUXO = linha[31:36]
    EMCVLREXPRISCO = linha[36:51]
    EMCMULTIPLOFATOR = linha[51:52]
    EMCCODGRUPO = linha[52:58]
    EMCSEMREGISTRO = linha[58:59]

    # Verifica se não há linhas em branco
    if linha == "" or linha is None:
        conn.execute(make_command("T1", nome_arquivo, n, "420"))
    # Verifica o tamanho padrão da linha (59 caracteres)
    if len(linha) != 59:
        conn.execute(make_command("T2", nome_arquivo, n, "420"))
    # Verifica se o campo sequencial EMCSEQ é uma sequência válida, que se
    # inicia em 000001
    if int(linha[0:6]) != n:
        conn.execute(make_command("T3", nome_arquivo, n, "420"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    if linha[6:10] != entcodigo:
        conn.execute(make_command("T4", nome_arquivo, n, "420"))
    # Verifica se o campo MRFMESANO corresponde, respectivamente, ao ano, mês
    # e último dia do mês de referência do FIP/SUSEP
    try:
        ciso8601.parse_datetime(linha[11:18])
    except ValueError:
        conn.execute(make_command("T5", nome_arquivo, n, "376"))
    # Verifica se o campo QUAID corresponde ao quadro 420
    if linha[12:21] == "420":
        conn.execute(make_command("T6", nome_arquivo, n, "420"))
    # Verifica se o campo DOCCODIGO corresponde a um tipo de direito ou
    # obrigação valido (conforme tabela “CONTRATOSEGUROCODIGO”)
    if linha[22:26] not in ["D0001", "D0002", "D0003", "D0004", "D0005",
                            "D0006", "D0007", "D9999", "CC001", "CC003",
                            "C0001", "C0002", "C0004", "C0005", "C0006",
                            "C9999", "CR001", "DR002", "CCP01", "CCP02",
                            "DCP01", "DCP02", "DCP03", "DCP04", "DCP05"]:
        conn.execute(make_command("T7", nome_arquivo, n, "420"))
    # Verifica se o campo TPFOPERADOR corresponde a um tipo de fluxo válido
    # (conforme tabela “TIPOFLUXO”)
    if linha[27] not in ["+", "-"]:
        conn.execute(make_command("T8", nome_arquivo, n, "420"))
    # Verifica se o campo FTRCODIGO corresponde a um tipo de fator válido
    # (conforme tabela "FATORCODIGO")
    if linha[28:30] not in ["JJ1", "JM1", "JM2", "JM3", "JM4", "JM9", "JT1",
                            "JT9", "JI1", "JI2", "JI8", "JI9", "ME1", "ME2",
                            "ME3", "ME4", "ME5", "ME9", "AA1", "AA2", "AA3",
                            "AA4", "AA9", "MC1", "TS1", "TS2", "TD1", "TD2",
                            "FF1", "PSR", "997", "998", "999", "IMO", "FII",
                            "DPV"]:
        conn.execute(make_command("T9", nome_arquivo, n, "420"))
    # Verifica se o campo EMCPRAZOFLUXO é um número inteiro positivo
    try:
        if not float(linha[31:35]) > 0:
            conn.execute(make_command("T10", nome_arquivo, n, "420"))
    except ValueError:
        conn.execute(make_command("T11", nome_arquivo, n, "420"))
    # Verifica se o campo EMCVLREXPRISCO é um número float positivo
    try:
        if not float(linha[36:50]) > 0:
            conn.execute(make_command("T12", nome_arquivo, n, "420"))
    except ValueError:
        conn.execute(make_command("T13", nome_arquivo, n, "420"))
    # Verifica se o campo EMCMULTIPLOFATOR é igual a 0 ou 1
    if linha[51] not in ["0", "1"]:
        conn.execute(make_command("T14", nome_arquivo, n, "420"))
    # Valida a correspondência entre os campos EMCCODGRUPO deste quadro com o
    # EMGCODGRUPO do quadro 423.
    pass
    # Valida a correspondência entre os campos DOCCODIGO e TPFOPERADOR
    if (linha[22:27] in ["D0001", "D0002", "D0003", "D0004",
                         "D0005", "D0006", "D0007", "D9999"] and
        linha[27] != "-") or \
        (linha[22:27] in ["C0001", "C0002", "C0004", "C0005",
                          "C0006", "C9999", "CR001"] and
         linha[27] != "+") or \
        (linha[22:27] == "DR002" and linha[27] != "-") or \
        (linha[22:27] in ["CCP01", "CCP02"] and
         linha[27] != "+") or \
        (linha[22:27] in ["DCP01", "DCP02", "DCP03", "DCP04",
                          "DCP05"] and linha[27] != "-"):
        conn.execute(make_command("T14", nome_arquivo, n, "420"))
    # Verifica se o campo EMCSEMREGISTRO é igual a 0 ou 1
    if linha[58] not in ["0", "1"]:
        conn.execute(make_command("T7", nome_arquivo, n, "420"))
