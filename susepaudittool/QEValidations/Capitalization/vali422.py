import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import make_command


# CAPITALIZAÇÃO
def validate_422(nome_arquivo, linha, n, conn, dates,
                 entcodigo):
    # Verifica se não há linhas em branco
    if linha == "" or linha is None:
        conn.execute(make_command("T1", nome_arquivo, n, "422"))
    # Verifica o tamanho padrão da linha (70 caracteres)
    if len(linha) != 70:
        conn.execute(make_command("T2", nome_arquivo, n, "422"))
    # Verifica se o campo sequencial EMESEQ é uma sequência válida, que se
    # inicia em 000001
    if int(linha[0:6]) == n:
        conn.execute(make_command("T3", nome_arquivo, n, "422"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    if linha[6:11] != entcodigo:
        conn.execute(make_command("T4", nome_arquivo, n, "422"))
    # Verifica se o campo MRFMESANO corresponde, respectivamente, ao ano, mês
    # e último dia do mês de referência do FIP/SUSEP
    if linha not in dates:
        conn.execute(make_command("T5", nome_arquivo, n, "422"))
    # Verifica se o campo QUAID corresponde ao quadro 422
    if linha[19:22] != "422":
        conn.execute(make_command("T6", nome_arquivo, n, "422"))
    # Verifica se o campo EMECODGRUPO é um número inteiro positivo
    try:
        if int(linha[22:28]) < 0:
            conn.execute(make_command("T7", nome_arquivo, n, "422"))
    except BaseException:
        conn.execute(make_command("T7", nome_arquivo, n, "422"))
    # Valida a correspondência entre os campos EMECODGRUPO deste quadro com o
    # EMGCODGRUPO do quadro 423
    pass
    # Verifica se o campo EMEPEF é um número float positivo
    try:
        if float(linha[28:43]) <= 0:
            conn.execute(make_command("T9", nome_arquivo, n, "422"))
    except BaseException:
        conn.execute(make_command("T9", nome_arquivo, n, "422"))
    # Verifica se o campo EMEVLRCONTATIVOS é um número float positivo
    try:
        if float(linha[43:58]) <= 0:
            conn.execute(make_command("T10", nome_arquivo, n, "422"))
    except BaseException:
        conn.execute(make_command("T10", nome_arquivo, n, "422"))
    # Verifica se o campo EMEPERCREVERSAO é um número float positivo
    try:
        if float(linha[58:64]) <= 0:
            conn.execute(make_command("T11", nome_arquivo, n, "422"))
    except BaseException:
        conn.execute(make_command("T11", nome_arquivo, n, "422"))
    # Verifica se o campo EMEPERCDEDUCAO é um número float positivo Sim
    try:
        if float(linha[64:70]) <= 0:
            conn.execute(make_command("T12", nome_arquivo, n, "422"))
    except BaseException:
        conn.execute(make_command("T12", nome_arquivo, n, "422"))