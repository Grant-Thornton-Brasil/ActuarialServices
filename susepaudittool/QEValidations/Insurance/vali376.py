import ciso8601
from ..tools import make_command


# SEGUROS
def validate_376(
    nome_arquivo, linha, n, conn, 
    dates, entcodigo, ramcodigos, esrcodcess):
    test14 = linha[88:93]
    
    tpmoids = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1012, 1013]
    # Verifica se não há linhas em branco
    try:
        if linha is None or linha == "":
            conn.execute(make_command("T1", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T1", nome_arquivo, n, "376"))

    # Verifica o tamanho padrão da linha (Deve conter 126 caracteres)
    try:
        if len(linha) != 126:
            conn.execute(make_command("T2", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T2", nome_arquivo, n, "376"))
    # Verifica se o campo sequencial ESRSEQ É uma sequência válida, que se
    # inicia em 000001
    try:
        if int(linha[0:7]) != n:
            conn.execute(make_command("T3", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T3", nome_arquivo, n, "376"))

    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    try:
        if linha[7:12] != entcodigo:
            conn.execute(make_command("T4", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T4", nome_arquivo, n, "376"))

    # Verifica se o campo MRFMESANO corresponde, respectivamente, ao ano, mês
    # e último dia do mês de referência do FIP/SUSEP
    try:
        if linha[12:20] not in dates:
            conn.execute(make_command("T5", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T5", nome_arquivo, n, "376"))
    # Verifica se o campo QUAID corresponde ao quadro 376
    try:
        if linha[20:23] != "376":
            conn.execute(make_command("T6", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T6", nome_arquivo, n, "376"))

    # Verifica se o campo TPMOID corresponde a um tipo de movimento válido
    try:
        if linha[23:27] not in ["0001", "0002", "0003", "0004", "0005", "0006", "0014"]:
            conn.execute(make_command("T7", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T7", nome_arquivo, n, "376"))

    # Valida a correspondência entre os campos TPMOID e CMPID
    try:
        if (
            linha[27:31]
            in [
                "1001",
                "1002",
                "1003",
                "1004",
                "1005",
                "1006",
                "1007",
                "1010",
                "1012",
                "1013",
            ]
            and linha[23:27] not in ["0001", "0002", "0003", "0004", "0005", "0006"]
        ) or (
            linha[27:31] in ["1011", "1014"]
            and linha[23:27]
            not in ["0001", "0002", "0003", "0004", "0005", "0006", "0014"]
        ):
            conn.execute(make_command("T8", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T8", nome_arquivo, n, "376"))
    # Verifica se o campo CMPID corresponde a um tipo de operação válida
    try:
        if linha[27:31] not in [
            "1001",
            "1002",
            "1003",
            "1004",
            "1005",
            "1006",
            "1007",
            "1008",
            "1009",
            "1010",
            "1011",
            "1012",
            "1013",
            "1014",
        ]:
            conn.execute(make_command("T9", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T9", nome_arquivo, n, "376"))
    # Verifica se o campo RAMCODIGO corresponde, respectivamente, a um grupo
    # de ramos e ramo válidos e operados pela companhia no mês de referência
    try:
        if linha[31:35] not in ramcodigos:
            conn.execute(make_command("T10", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T10", nome_arquivo, n, "376"))
    # Verifica se o campo RAMCODIGO não foi preenchido com os ramos 0588,
    # 0589, 0983, 0986, 0991, 0992, 0994, 0996, 1066, 1383, 1386, 1391, 1392,
    # 1396, 1603 e 2201
    try:
        if linha[27:31] in [
            "583",
            "588",
            "589",
            "983",
            "986",
            "991",
            "992",
            "994",
            "1066",
            "1286",
            "1383",
            "1386",
            "1391",
            "1392",
            "1603",
        ]:
            conn.execute(make_command("T11", nome_arquivo, n, "376"))
    except BaseException:
        conn.execute(make_command("T11", nome_arquivo, n, "376"))
    # Verifica se o valor dos campos ESRVALORMOV e ESRVALORMON é float
    try:
        float(linha[67:80].replace(",", "."))
        float(linha[113:126].replace(",", "."))
    except ValueError:
        conn.execute(make_command("T12", nome_arquivo, n, "376"))
    # Verifica se os campos ESRDATAINICIO, ESRDATAFIM, ESRDATAOCORR,
    # ESRDATAREG e ESRDATACOMUNICA correspondem a uma data válida
    try:
        ciso8601.parse_datetime(linha[35:43])
        ciso8601.parse_datetime(linha[43:51])
        ciso8601.parse_datetime(linha[51:59])
        ciso8601.parse_datetime(linha[59:67])
        ciso8601.parse_datetime(linha[80:88])
    except ValueError:
        conn.execute(make_command("T13", nome_arquivo, n, "376"))
