import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import make_command


# CAPITALIZAÇÃO
def validate_423(nome_arquivo, linha, n, conn, dates,
                 entcodigo):
    EMGSEQ = linha[0:6]
    ENTCODIGO = linha[6:11]
    MRFMESANO = linha[11:19]
    QUAID = linha[19:22]
    EMGCODGRUPO = linha[22:28]
    RAMCODIGO = linha[28:32]
    PLNCODIGO = linha[32:38]

    # Verifica se não há linhas em branco
    if linha == "" or linha is None:
        conn.execute(make_command("T1", nome_arquivo, n, "423"))
    # Verifica o tamanho padrão da linha (38 caracteres)
    if len(linha) != 38:
        conn.execute(make_command("T2", nome_arquivo, n, "423"))
    # Verifica se o campo sequencial EMGSEQ é uma sequência válida, que se
    # inicia em 000001
    if int(linha[0:6]) != n:
        conn.execute(make_command("T3", nome_arquivo, n, "423"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    if linha[6:11] != entcodigo:
        conn.execute(make_command("T4", nome_arquivo, n, "423"))
    # Verifica se o campo MRFMESANO corresponde, respectivamente, ao ano, mês
    # e último dia do mês de referência do FIP/SUSEP
    if linha[11:19] not in dates:
        conn.execute(make_command("T5", nome_arquivo, n, "423"))
    # Verifica se o campo QUAID corresponde ao quadro 423
    if linha[19:22] != "423":
        conn.execute(make_command("T6", nome_arquivo, n, "423"))
    # Verifica se o campo EMGCODGRUPO é um número inteiro positivo
    try:
        if float(linha[22:28]) <= 0:
            conn.execute(make_command("T7", nome_arquivo, n, "423"))
    except BaseException:
        conn.execute(make_command("T7", nome_arquivo, n, "423"))
    # Valida a correspondência entre os campos ENTCODIGO e RAMCODIGO, exceto
    # para preenchimentos com zeros do RAMCODIGO
    pass
    # Valida a correspondência entre o campo PLNCODIGO e a tabela Planos do
    # FIP/SUSEP, exceto para preenchimentos com zeros do PLNCODIGO
    pass
    # Verifica se o campo PLNCODIGO ou o RAMCODIGO está preenchido diferente
    # de zeros, porém não ambos ao mesmo tempo
    if int(linha[32:38]) == 0 or \
       int(linha[28:32]) == 0 or \
       (int(linha[32:38]) == 0 and int(linha[28:32]) == 0):
        conn.execute(make_command("T10", nome_arquivo, n, "423"))
