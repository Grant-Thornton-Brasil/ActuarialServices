import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import make_command


# CAPITALIZAÇÃO
def validate_421(nome_arquivo, linha, n, conn, dates,
                 entcodigo):
    EMDSEQ = linha[0:6]
    ENTCODIGO = linha[6:11]
    MRFMESANO = linha[11:19]
    QUAID = linha[19:22]
    DODCODIGO = linha[22:27]
    TPFOPERADOR = linha[27:28]
    FTRCODIGO = linha[28:31]
    EMDPRAZOFLUXO = linha[31:36]
    EMDVLREXPRISCO = linha[36:51]
    EMDMULTIPLOFATOR = linha[51:52]

    # Verifica se não há linhas em branco
    if linha == "" or linha is None:
        conn.execute(make_command("T1", nome_arquivo, n, "421"))
    #  Verifica o tamanho padrão da linha (52 caracteres)
    if len(linha) != 52:
        conn.execute(make_command("T2", nome_arquivo, n, "421"))
    # Verifica se o campo sequencial EMDSEQ é uma sequência válida, que se
    # inicia em 000001
    if int(EMDSEQ) != n:
        conn.execute(make_command("T3", nome_arquivo, n, "421"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    if ENTCODIGO != entcodigo:
        conn.execute(make_command("T4", nome_arquivo, n, "421"))
    # Verifica se o campo MRFMESANO corresponde, respectivamente, ao ano, mês
    # e último dia do mês de referência do FIP/SUSEP
    if MRFMESANO not in dates:
        conn.execute(make_command("T5", nome_arquivo, n, "421"))
    #  Verifica se o campo QUAID corresponde ao quadro 421
    if QUAID != "421":
        conn.execute(make_command("T6", nome_arquivo, n, "421"))
    # Verifica se o campo DODCODIGO corresponde a um tipo de obrigação ou
    # direito válido (conforme tabela "DEMAISCODIGO")
    if DODCODIGO not in ["C0001", "C0002", "C0003",
                            "C9999", "D0001", "D0002", "D0003", "D9999"]:
        conn.execute(make_command("T7", nome_arquivo, n, "421"))
    # Verifica se o campo TPFOPERADOR corresponde a um tipo de fluxo válido
    # (conforme tabela “TIPOFLUXO”)
    if TPFOPERADOR not in ["+", "-"]:
        conn.execute(make_command("T8", nome_arquivo, n, "421"))
    # Verifica se o campo FTRCODIGO corresponde a um tipo de fator válido
    # (conforme tabela "FATORCODIGO")
    if FTRCODIGO not in ["JJ1", "JM1", "JM2", "JM3", "JM4", "JM9", "JT1",
                            "JT9", "JI1", "JI2", "JI8", "JI9", "ME1", "ME2",
                            "ME3", "ME4", "ME5", "ME9", "AA1", "AA2", "AA3",
                            "AA4", "AA9", "MC1", "TS1", "TS2", "TD1", "TD2",
                            "FF1", "PSR", "997", "998", "999", "IMO", "FII",
                            "DPV"]:
        conn.execute(make_command("T9", nome_arquivo, n, "421"))
    #  Verifica se o campo EMDPRAZOFLUXO é um número inteiro positivo
    try:
        if not int(EMDPRAZOFLUXO) > 0:
            conn.execute(make_command("T10", nome_arquivo, n, "421"))
    except ValueError:
        conn.execute(make_command("T10", nome_arquivo, n, "421"))
    #  Verifica se o campo EMDVLREXPRISCO é um número float positivo
    try:
        if not float(EMDVLREXPRISCO) > 0:
            conn.execute(make_command("T11", nome_arquivo, n, "421"))
    except ValueError:
        conn.execute(make_command("T11", nome_arquivo, n, "421"))
    #  Verifica se o campo EMDMULTIPLOFATOR é igual a 0 ou 1
    if EMDMULTIPLOFATOR not in ["0", "1"]:
        conn.execute(make_command("T12", nome_arquivo, n, "421"))
    #  Valida a correspondência entre os campos DODCODIGO e TPFOPERADOR
    if (DODCODIGO in ["C0001", "C0002", "C0003", "C9999"] and
        TPFOPERADOR != "+") or \
       (DODCODIGO in ["D0001", "D0002", "D0003", "D9999"] and
        TPFOPERADOR != "-"):
        conn.execute(make_command("T13", nome_arquivo, n, "421"))
