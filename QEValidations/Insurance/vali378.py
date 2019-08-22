import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import make_command


# SEGUROS
def validate_378(nome_arquivo, linha, n, conn, dates,
                 entcodigo, ramcodigos, esrcodcess):
    # 1	Verifica se não há linhas em branco
    if linha is None or linha == "":
        conn.execute(make_command("T1", nome_arquivo, n, "378"))

    # Verifica o tamanho padrão da linha (deve conter 173 caracteres)
    if len(linha) != 173:
        conn.execute(make_command("T2", nome_arquivo, n, "378"))

    # Verifica se o campo sequencial ESPSEQ é uma sequência válida, que se
    # inicia em 0000001
    if int(linha[0:7]) != n:
        conn.execute(make_command("T3", nome_arquivo, n, "378"))

    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    if linha[7:12] != entcodigo:
        conn.execute(make_command("T4", nome_arquivo, n, "378"))

    # Verifica se o campo MRFMESANO corresponde, respectivamente, ao ano, mês
    # e último dia do mês de referência do FIP/SUSEP
    if linha[12:20] not in dates:
        conn.execute(make_command("T5", nome_arquivo, n, "378"))

    # Verifica se o campo QUAID corresponde ao quadro 378
    if linha[20:23] != "378":
        conn.execute(make_command("T6", nome_arquivo, n, "378"))

    # Verifica se o campo TPMOID corresponde a um tipo de movimento válido
    # (conforme tabela 'TiposMovimentos' do FIPSUSEP)
    if linha[23:27] not in ["0007", "0008", "0009", "0010"]:
        conn.execute(make_command("T7", nome_arquivo, n, "378"))

    # Valida a correspondência entre os campos TPMOID e CMPID
    if (linha[23:27] in ["0007",
                         "0008"] and linha[27:31] not in ["1026", "1027",
                                                          "1028", "1029"]) or \
        (linha[23:27] == "0009" and linha[27:31] not in ["1030", "1031",
                                                         "1032", "1033"]) or \
        (linha[23:27] == "0010" and linha[27:31] not in ["1034", "1035",
                                                         "1036", "1037"]):
        conn.execute(make_command("T8", nome_arquivo, n, "378"))

    # Verifica se o campo CMPID corresponde a um tipo de operação válida
    # (conforme tabela 'Bib_DefCamposEstatísticos do FIPSUSEP)
    if int(linha[27:31]) not in [i for i in range(1026, 1038)]:
        conn.execute(make_command("T9", nome_arquivo, n, "378"))

    # Verifica se o campo RAMCODIGO corresponde, respectivamente, a um grupo
    # de ramos e ramo válidos
    if linha[31:35] not in ramcodigos:
        conn.execute(make_command("T10", nome_arquivo, n, "378"))

    # Verifica se o campo RAMCODIGO não foi preenchido para os ramos 0588,
    # 0589, 0983, 0986, 0991, 0992, 0994, 0996, 1066, 1383, 1386, 1391, 1392,
    # 1396, 1603 e 2201
    if int(linha[27:31]) in [583, 588, 589, 983, 986, 991, 992, 994,
                             1066, 1286, 1383, 1386, 1391, 1392, 1603]:
        conn.execute(make_command("T11", nome_arquivo, n, "378"))

    # Verifica se o valor dos campos ESPVALORMOVRO, ESPVALORMOVRD,
    # ESPVALORCARO, ESPVALORCARD, ESPVALORCIRO e ESPVALORCIRD é float
    try:
        float(linha[59:72].replace(",", "."))
        float(linha[96:109].replace(",", "."))
        float(linha[118:131].replace(",", "."))
        float(linha[131:144].replace(",", "."))
        float(linha[144:157].replace(",", "."))
        float(linha[157:170].replace(",", "."))
    except ValueError:
        conn.execute(make_command("T12", nome_arquivo, n, "378"))

    # Verifica se os campos ESPDATAINICIORO, ESPDATAFIMRO, ESPEMISSRO,
    # ESPDATAINICIORD, ESPDATAFIMRD e ESPEMISSRD correspondem a uma data
    # válida
    try:
        ciso8601.parse_datetime(linha[35:43])
        ciso8601.parse_datetime(linha[43:51])
        ciso8601.parse_datetime(linha[51:59])
        ciso8601.parse_datetime(linha[72:80])
        ciso8601.parse_datetime(linha[80:88])
        ciso8601.parse_datetime(linha[88:96])
    except ValueError:
        conn.execute(make_command("T13", nome_arquivo, n, "378"))