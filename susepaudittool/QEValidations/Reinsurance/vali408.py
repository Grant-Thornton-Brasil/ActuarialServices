import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import *

moedas = get_moedas()


# RESEGUROS
def validate_408(nome_arquivo, linha, n, conn, dates,
                 entcodigo, gracodigos):

    MPASEQ = int(linha[0:7])
    ENTCODIGO = linha[7:12]
    MRFMESANO = linha[12:18]
    TPMORESSID = linha[18:21]
    GRACODIGO = linha[21:23]
    MPATIPOPERA = linha[23:24]
    MPANUMCONT = linha[24:50]
    MPANUMENDOSSO = linha[50:56]
    MPACODCESS = linha[56:61]
    MPATIPOCONT = linha[61:62]
    MPAMODCONT = linha[62:64]
    MPADATAORDEMFIRME = linha[64:72]
    MPADATACONTR = linha[72:80]
    MPADATAINICIO = linha[80:88]
    MPADATAFIM = linha[88:96]
    MPAVALORMOV = linha[96:109]
    MPAPERCENTRISCO = linha[109:115]
    MPAVALORMOVCOMIS = linha[115:128]
    MPAVALORMOVCORRET = linha[128:141]
    MPACODCORRET = linha[141:146]
    MPAVIGMED = linha[146:148]
    MPABASEIND = linha[148:149]
    MPAMOEDA = linha[149:152]
    MPATAXACONV = linha[152:165]
    MPADATAEMISS = linha[165:173]

    # Verifica se não há linhas em branco
    try:
        if linha == "" or linha is None:
            conn.execute(make_command("T1", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T1", nome_arquivo, n, "408"))
    # Verifica o tamanho padrão da linha (deve conter 173 caracteres)
    try:
        if len(linha) != 173:
            conn.execute(make_command("T2", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T2", nome_arquivo, n, "408"))
    # Verifica se o campo sequencial MPASEQ é uma sequência válida, que se
    # inicia em 0000001
    try:
        if MPASEQ != n:
            conn.execute(make_command("T3", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T3", nome_arquivo, n, "408"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    try:
        if ENTCODIGO != entcodigo:
            conn.execute(make_command("T4", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T4", nome_arquivo, n, "408"))
    # Verifica se o campo MRFMESANO corresponde a um ano e mês válidos
    try:
        ciso8601.parse_datetime(MRFMESANO + "01")
    except ValueError:
        conn.execute(make_command("T5", nome_arquivo, n, "408"))
    # Verifica se o campo TPMORESSID corresponde a um tipo de movimento válido
    # (conforme tabela 'TiposMovimentosResseguros' do FIPSUSEP)
    try:
        if TPMORESSID not in ["024", "025", "026", "027", "028", "029",
                                "030", "031", "032", "033", "034"]:
            conn.execute(make_command("T6", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T6", nome_arquivo, n, "408"))
    # Verifica se o campo GRACODIGO corresponde a um grupo de ramos válido
    # operado pelo ressegurador
    try:
        if GRACODIGO not in gracodigos:
            conn.execute(make_command("T7", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T7", nome_arquivo, n, "408"))
    # Verifica se o campo MPATIPOPERA foi preenchido com um tipo de operação
    # válido
    try:
        if MPATIPOPERA not in ["1", "2"]:
            conn.execute(make_command("T8", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T8", nome_arquivo, n, "408"))
    # Verifica se o campo MPACODCESS corresponde a um código de sociedade
    # válido ou ‘99999’ e valida a correspondência entre os campos MPATIPOPERA
    # e MPACODCESS
    try:
        if (linha[23] == "1" and int(linha[56:61]) not in [i for i in range(1, 20000)]) or (
                linha[23] == "2" and int(linha[56:61]) not in [i for i in range(30000, 60000)]):
            conn.execute(make_command("T9", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T9", nome_arquivo, n, "408"))
    # Verifica se o campo MPATIPOCONT foi preenchido com um tipo de contrato
    # válido
    try:
        if MPATIPOCONT not in ["1", "2"]:
            conn.execute(make_command("T10", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T10", nome_arquivo, n, "408"))
    # Verifica se o campo MPAMODCONT foi preenchido com uma modalidade de
    # contrato válida, exceto nos casos em que o tipo de contrato seja
    # ‘Facultativo’, quando o campo deve ser preenchido com ‘99’
    try:
        if (linha[61] == "1" and linha[62:64] not in ["01", "02", "03",
                                                        "04", "05", "06"]) \
                or (linha[61] == "2" and linha[62:64] != "99"):
            conn.execute(make_command("T11", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T11", nome_arquivo, n, "408"))
    # Para o tipo de contrato 'Facultativo', verifica se o tipo de movimento é
    # 'Emissão de Prêmio Efetivo' ou 'Endosso de Prêmio Efetivo' ou
    # 'Restituição de Prêmio Efetivo' ou 'Cancelamento de Prêmio Efetivo' ou
    # 'Informação sem Movimentação de Prêmio'
    try:
        if MPATIPOCONT == "2" and TPMORESSID not in ["024", "025", "026", "027", "034"]:
            conn.execute(make_command("T12", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T12", nome_arquivo, n, "408"))
    # Para o tipo de contrato 'Automático' e para as modalidades de contrato
    # 'Proporcional', verifica se o tipo de movimento é 'Emissão de Prêmio
    # Efetivo' ou 'Endosso de Prêmio Efetivo' ou 'Restituição de Prêmio
    # Efetivo' ou 'Cancelamento de Prêmio Efetivo' ou 'Ajuste de Prêmio
    # Efetivo' ou 'Emissão de Prêmio Estimado' ou 'Alteração de Prêmio
    # Estimado' ou 'Cancelamento de Prêmio Estimado' ou 'Ajuste de Prêmio
    # Estimado' ou 'Informação sem Movimentação de Prêmio'
    try:
        if linha[61] == "1" and linha[62:64] in [
                "1", "2"] and linha[18:21] not in [""]:
            conn.execute(make_command("T13", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T13", nome_arquivo, n, "408"))
    # Para o tipo de contrato 'Automático' e para as modalidades de contrato
    # 'Não Proporcional' e 'Clash', verifica se o tipo de movimento é 'Emissão
    # de Prêmio Efetivo' ou 'Endosso de Prêmio Efetivo' ou 'Restituição de
    # Prêmio Efetivo' ou 'Cancelamento de Prêmio Efetivo' ou 'Ajuste de Prêmio
    # Efetivo' ou 'Prêmio de Reintegração' ou 'Informação sem Movimentação de
    # Prêmio'
    pass
    # Verifica se os campos MPADATAORDEMFIRME, MPADATAINICIO, MPADATAFIM e
    # MPADATAEMISS correspondem a uma data válida
    try:
        ciso8601.parse_datetime(MPADATAORDEMFIRME)
        ciso8601.parse_datetime(MPADATAINICIO)
        ciso8601.parse_datetime(MPADATAFIM)
        ciso8601.parse_datetime(MPADATAEMISS)
    except ValueError:
        conn.execute(make_command("T15", nome_arquivo, n, "408"))
    # Verifica se o campo MPADATACONTR foi preenchido com uma data válida ou
    # com '99999999
    try:
        if linha[72:80] != "99999999":
            try:
                ciso8601.parse_datetime(linha[72:80])
            except ValueError:
                conn.execute(make_command("T16", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T16", nome_arquivo, n, "408"))
    # Verifica se o valor dos campos MPAVALORMOV, MPAVALORMOVCOMIS,
    # MPAVALORMOVCORRET e MPATAXACONV é float
    try:
        float(MPAVALORMOV.replace(",", ""))
        float(MPAVALORMOVCOMIS.replace(",", ""))
        float(MPAVALORMOVCORRET.replace(",", ""))
        float(MPATAXACONV.replace(",", ""))
    except ValueError:
        conn.execute(make_command("T17", nome_arquivo, n, "408"))
    # Verifica se o campo MPAPERCENTRISCO corresponde a um valor entre
    # '000,01' e '100,00'
    try:
        if (0.01 <= float(MPAPERCENTRISCO.replace(",", ".")) <= 100) == False:
            conn.execute(make_command("T18", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T18", nome_arquivo, n, "408"))
    # Verifica se o campo MPACODCORRET corresponde a um código de corretora de
    # resseguro válido ou '99999'
    try:
        if (not (70000 <= int(MPACODCORRET) <= 79999)):
            if MPACODCORRET != "99999":
                conn.execute(make_command("T19", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T19", nome_arquivo, n, "408"))
    # Verifica se o campo MPAVIGMED corresponde a um valor entre '01' e '99'
    try:
        if (1 <= int(MPAVIGMED) <= 99) == False:
            conn.execute(make_command("T20", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T20", nome_arquivo, n, "408"))
    # Verifica se o campo MPABASEIND foi preenchido com uma base indenitária
    # válida
    try:
        if MPABASEIND not in ["1", "2", "3"]:
            conn.execute(make_command("T21", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T21", nome_arquivo, n, "408"))
    # Verifica se o campo MPAMOEDA foi preenchido com uma moeda válida
    try:
        if MPAMOEDA not in moedas:
            conn.execute(make_command("22", nome_arquivo, n, "408"))
    except:
        conn.execute(make_command("T22", nome_arquivo, n, "408"))