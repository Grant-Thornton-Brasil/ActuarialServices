import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import make_command


# RESEGUROS
def validate_408(nome_arquivo, linha, n, conn, dates,
                 entcodigo, gracodigos):
    # Verifica se não há linhas em branco
    if linha == "" or linha is None:
        conn.execute(make_command("T1", nome_arquivo, n, "408"))
    # Verifica o tamanho padrão da linha (deve conter 173 caracteres)
    if len(linha) != 173:
        conn.execute(make_command("T2", nome_arquivo, n, "408"))
    # Verifica se o campo sequencial MPASEQ é uma sequência válida, que se
    # inicia em 0000001
    if int(linha[0:7]) != n:
        conn.execute(make_command("T3", nome_arquivo, n, "408"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    if linha[7:12] != entcodigo:
        conn.execute(make_command("T4", nome_arquivo, n, "408"))
    # Verifica se o campo MRFMESANO corresponde a um ano e mês válidos
    try:
        ciso8601.parse_datetime(linha[12:18] + "01")
    except ValueError:
        conn.execute(make_command("T5", nome_arquivo, n, "408"))
    # Verifica se o campo TPMORESSID corresponde a um tipo de movimento válido
    # (conforme tabela 'TiposMovimentosResseguros' do FIPSUSEP)
    if linha[18:21] not in ["024", "025", "026", "027", "028", "029",
                            "030", "031", "032", "033"]:
        conn.execute(make_command("T6", nome_arquivo, n, "408"))
    # Verifica se o campo GRACODIGO corresponde a um grupo de ramos válido
    # operado pelo ressegurador
    if linha[21:23] not in gracodigos:
        conn.execute(make_command("T7", nome_arquivo, n, "408"))
    # Verifica se o campo MPATIPOPERA foi preenchido com um tipo de operação
    # válido
    if linha[23:24] not in ["1", "2"]:
        conn.execute(make_command("T8", nome_arquivo, n, "408"))
    # Verifica se o campo MPACODCESS corresponde a um código de sociedade
    # válido ou ‘99999’ e valida a correspondência entre os campos MPATIPOPERA
    # e MPACODCESS
    if (linha[23] == "1" and int(linha[56:61]) not in [i for i in range(1, 20000)]) or (
            linha[23] == "2" and int(linha[56:61]) not in [i for i in range(30000, 60000)]):
        conn.execute(make_command("T9", nome_arquivo, n, "408"))
    # Verifica se o campo MPATIPOCONT foi preenchido com um tipo de contrato
    # válido
    if linha[61:62] not in ["1", "2"]:
        conn.execute(make_command("T10", nome_arquivo, n, "408"))
    # Verifica se o campo MPAMODCONT foi preenchido com uma modalidade de
    # contrato válida, exceto nos casos em que o tipo de contrato seja
    # ‘Facultativo’, quando o campo deve ser preenchido com ‘99’
    if (linha[61:62] == "1" and linha[62:64] not in ["01", "02", "03",
                                                     "04", "05", "06"]) \
            or (linha[61:62] == "2" and linha[62:64] != "99"):
        conn.execute(make_command("T11", nome_arquivo, n, "408"))
    # Para o tipo de contrato 'Facultativo', verifica se o tipo de movimento é
    # 'Emissão de Prêmio Efetivo' ou 'Endosso de Prêmio Efetivo' ou
    # 'Restituição de Prêmio Efetivo' ou 'Cancelamento de Prêmio Efetivo' ou
    # 'Informação sem Movimentação de Prêmio'
    pass
    # Para o tipo de contrato 'Automático' e para as modalidades de contrato
    # 'Proporcional', verifica se o tipo de movimento é 'Emissão de Prêmio
    # Efetivo' ou 'Endosso de Prêmio Efetivo' ou 'Restituição de Prêmio
    # Efetivo' ou 'Cancelamento de Prêmio Efetivo' ou 'Ajuste de Prêmio
    # Efetivo' ou 'Emissão de Prêmio Estimado' ou 'Alteração de Prêmio
    # Estimado' ou 'Cancelamento de Prêmio Estimado' ou 'Ajuste de Prêmio
    # Estimado' ou 'Informação sem Movimentação de Prêmio'
    if linha[61] == "1" and linha[62:64] in [
            "1", "2"] and linha[18:21] not in [""]:
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
        ciso8601.parse_datetime(linha[64:72])
        ciso8601.parse_datetime(linha[80:88])
        ciso8601.parse_datetime(linha[88:96])
    except ValueError:
        conn.execute(make_command("T15", nome_arquivo, n, "408"))
    # Verifica se o campo MPADATACONTR foi preenchido com uma data válida ou
    # com '99999999
    if linha[72:80] != "99999999":
        try:
            ciso8601.parse_datetime(linha[72:80])
        except ValueError:
            conn.execute(make_command("T16", nome_arquivo, n, "408"))
    # Verifica se o valor dos campos MPAVALORMOV, MPAVALORMOVCOMIS,
    # MPAVALORMOVCORRET e MPATAXACONV é float
    try:
        float(linha[96:109].replace(",", ""))
        float(linha[115:128].replace(",", ""))
        float(linha[128:141].replace(",", ""))
        float(linha[152:165].replace(",", ""))
    except ValueError:
        conn.execute(make_command("T17", nome_arquivo, n, "408"))
    # Verifica se o campo MPAPERCENTRISCO corresponde a um valor entre
    # '000,01' e '100,00'
    if (0.01 <= float(linha[109:115].replace(",", ".")) <= 100) == False:
        conn.execute(make_command("T18", nome_arquivo, n, "408"))
    # Verifica se o campo MPACODCORRET corresponde a um código de corretora de
    # resseguro válido ou '99999'
    if not (70000 <= int(linha[141:146]) <=
            79999) or linha[141:146] == "99999":
        conn.execute(make_command("T19", nome_arquivo, n, "408"))
    # Verifica se o campo MPAVIGMED corresponde a um valor entre '01' e '99'
    if (1 <= int(linha[146:148]) <= 99) == False:
        conn.execute(make_command("T20", nome_arquivo, n, "408"))
    # Verifica se o campo MPABASEIND foi preenchido com uma base indenitária
    # válida
    if linha[148] not in ["1", "2", "3"]:
        conn.execute(make_command("T21", nome_arquivo, n, "408"))
    # Verifica se o campo MPAMOEDA foi preenchido com uma moeda válida
    if linha[149:152] not in moedas:
        conn.execute(make_command("22", nome_arquivo, n, "408"))