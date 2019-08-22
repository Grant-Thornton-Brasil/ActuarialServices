import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import make_command


# SEGUROS
def validate_377(nome_arquivo, linha, n, conn, dates,
                 entcodigo, ramcodigos, esrcodcess):
    # Verifica se não há linhas em branco
    if linha is None or linha == "":
        conn.execute(make_command("T1", nome_arquivo, n, "377"))

    # Verifica o tamanho padrão da linha (deve conter 101 caracteres).
    if len(linha) != 101:
        conn.execute(make_command("T2", nome_arquivo, n, "377"))

    # Verifica se o campo sequencial ESRSEQ é uma sequência válida, que se
    # inicia em 0000001.
    if int(linha[0:7]) != n:
        conn.execute(make_command("T3", nome_arquivo, n, "377"))

    # Verifica se o campo ENTCODIGO corresponde à sociedade que está
    # enviando o FIP/SUSEP.
    if linha[7:12] != entcodigo:
        conn.execute(make_command("T4", nome_arquivo, n, "377"))

    # Verifica se o campo MRFMESANO corresponde, respectivamente,
    # ao ano, mês e último dia do mês de referência do FIP/SUSEP.
    if linha[12:20] not in dates:
        conn.execute(make_command("T5", nome_arquivo, n, "377"))

    # Verifica se o campo QUAID corresponde ao quadro 377.
    if linha[20:23] != "377":
        conn.execute(make_command("T6", nome_arquivo, n, "377"))

    # Verifica se o campo CMPID corresponde a um tipo de operação válida
    # (conforme tabela Bib_DefCamposEstatísticos).
    if int(linha[23:27]) not in [i for i in range(1015, 1026)]:
        conn.execute(make_command("T7", nome_arquivo, n, "377"))

    # Verifica se o campo RAMCODIGO corresponde, respectivamente, a um grupo
    # de ramos e ramo válidos e operados pela companhia no mês de referência.
    if linha[27:31] not in ramcodigos:
        conn.execute(make_command("T8", nome_arquivo, n, "377"))

    # 9	Verifica se o campo RAMCODIGO não foi preenchido para os ramos
    #  0588, 0589, 0983, 0986, 0991, 0992, 0994, 0996, 1066, 1383, 1386,
    #  1391, 1392, 1396, 1603 e 2201.
    if int(linha[27:31]) in [583, 588, 589, 983, 986, 991, 992, 994,
                             1066, 1286, 1383, 1386, 1391, 1392, 1603]:
        conn.execute(make_command("T9", nome_arquivo, n, "377"))

    # 10 Verifica se o valor dos campos ESLVALORMOV é float.
    try:
        float(linha[63:76].replace(",", "."))
    except ValueError:
        conn.execute(make_command("T10", nome_arquivo, n, "377"))

    # 11 Verifica se os campos ESLDATAINICIO, ESLDATAFIM, ESLDATAOCORR e
    # ESLDATAREG correspondem a uma data válida.
    try:
        ciso8601.parse_datetime(linha[31:39])
        ciso8601.parse_datetime(linha[39:47])
        ciso8601.parse_datetime(linha[47:55])
        ciso8601.parse_datetime(linha[55:63])
    except ValueError:
        conn.execute(make_command("T11", nome_arquivo, n, "377"))