import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import *

moedas = get_moedas()


# RESEGUROS
def validate_404(nome_arquivo, linha, n, conn, dates,
                 entcodigo, gracodigos):
    # Verifica se não há linhas em branco
    try:
        if linha == "" or linha is None:
            conn.execute(make_command("T1", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T1", nome_arquivo, n, "404"))
    # Verifica o tamanho padrão da linha (deve conter 133 caracteres)
    try:
        if len(linha) != 133:
            conn.execute(make_command("T2", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T2", nome_arquivo, n, "404"))
    # Verifica se o campo sequencial MSASEQ é uma sequência válida, que se
    # inicia em 0000001
    try:
        if int(linha[0:7]) != n:
            conn.execute(make_command("T3", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T3", nome_arquivo, n, "404"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    try:
        if linha[7:12] != entcodigo:
            conn.execute(make_command("T4", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T4", nome_arquivo, n, "404"))
    # Verifica se o campo MRFMESANO corresponde a um ano e mês válidos
    try:
        ciso8601.parse_datetime(linha[12:18] + "01")
    except ValueError:
        conn.execute(make_command("T5", nome_arquivo, n, "404"))
    # Verifica se o campo TPMORESSID corresponde a um tipo de movimento válido
    # (conforme tabela 'TiposMovimentosResseguros' do FIPSUSEP)
    try:
        if linha[18:21] not in ["001", "002", "003", "004",
                                "005", "006", "007", "008", "009", "010", "011"]:
            conn.execute(make_command("T6", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T6", nome_arquivo, n, "404"))
    # Verifica se o campo GRACODIGO corresponde a um grupo de ramos válido
    # operado pelo ressegurador
    try:
        if linha[21:23] not in gracodigos:
            conn.execute(make_command("T7", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T7", nome_arquivo, n, "404"))
    # Verifica se o campo MSATIPOPERA foi preenchido com um tipo de operação
    # válido
    try:
        if linha[23] not in ["1", "2"]:
            conn.execute(make_command("T8", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T8", nome_arquivo, n, "404"))
    # Verifica se o campo MSATIPOCONT foi preenchido com um tipo de contrato
    # válido
    try:
        if linha[70] not in ["1", "2"]:
            conn.execute(make_command("T9", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T9", nome_arquivo, n, "404"))
    # Verifica se o campo MSACODCESS corresponde a um código de sociedade
    # válido ou ‘99999’ e valida a correspondência entre os campos MSATIPOPERA
    # e MSACODCESS
    try:
        if (linha[23] == "1" and not (1 <= int(linha[71:76]) <= 19999)) or \
            (linha[23] == "2" and not (30000 <= int(linha[71:76]) <= 59999)) or \
                linha[71:76] == "99999":
            conn.execute(make_command("T10", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T10", nome_arquivo, n, "404"))
    # Verifica se os campos MSADATAOCORR, MSADATACOMUNICA e MSADATAREG
    # correspondem a uma data válida. Nos casos em que a modalidade do
    # contrato seja 'Proporcional: cota parte' ou 'Proporcional: ER', os
    # campos podem ser preenchidos com '99999999'
    try:
        if linha[114:116] in ["01", "02"]:
            if linha[76:84] != "99999999" or \
                linha[84:92] != "99999999" or \
                    linha[92:100] != "99999999":
                conn.execute(make_command("T11", nome_arquivo, n, "404"))
        else:
            try:
                ciso8601.parse_datetime(linha[76:84])
                ciso8601.parse_datetime(linha[84:92])
                ciso8601.parse_datetime(linha[92:100])
            except ValueError:
                conn.execute(make_command("T11", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T11", nome_arquivo, n, "404"))
    # Verifica se o valor dos campos MSAVALORMOV e MSAVALORMON é float
    try:
        float(linha[100:113].replace(",", "."))
        float(linha[120:133].replace(",", "."))
    except ValueError:
        conn.execute(make_command("T12", nome_arquivo, n, "404"))
    # Verifica se o campo MSATIPOSIN foi preenchido com um tipo de sinistro
    # válido
    try:
        if int(linha[113:114]) not in [1, 2]:
            conn.execute(make_command("T13", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T13", nome_arquivo, n, "404"))
    # Verifica se o campo MSAMODCONT foi preenchido com uma modalidade de
    # contrato válida, exceto nos casos em que o tipo de contrato seja
    # ‘Facultativo’, quando o campo deve ser preenchido com ‘99’
    try:
        if (linha[70] == "2" and linha[114:116] != "99") and linha[114:116] not in [
                "01", "02", "03", "04", "05", "06"]:
            conn.execute(make_command("T14", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T14", nome_arquivo, n, "404"))
    # Verifica se o campo MSAMOEDA foi preenchido com uma moeda válida
    try:
        if linha[116:119] not in moedas:
            conn.execute(make_command("T15", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T15", nome_arquivo, n, "404"))
    # Verifica se o campo MSABASEIND foi preenchido com uma base indenitária
    # válida
    try:
        if linha[119:120] not in ["1", "2", "3"]:
            conn.execute(make_command("T16", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T16", nome_arquivo, n, "404"))