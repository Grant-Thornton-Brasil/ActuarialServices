import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import *

moedas = get_moedas()


# RESEGUROS
def validate_409(nome_arquivo, linha, n, conn, dates,
                 entcodigo, gracodigos):
    MPRSEQ = linha[0:7]
    ENTCODIGO = linha[7:12]
    MRFMESANO = linha[12:18]
    TPMORESSID = linha[18:21]
    GRACODIGO = linha[21:23]
    MPRNUMCONT = linha[23:49]
    MPRNUMENDOSSO = linha[49:55]
    MPRCODESS = linha[55:60]
    MPRTIPOCONT = linha[60:61]
    MPRMODCONT = linha[61:63]
    MPRDATACEITE = linha[63:71]
    MPRDATACONTR = linha[71:79]
    MPRDATAINICIO = linha[79:87]
    MPRDATAFIM = linha[87:95]
    MPRPERCRISCO = linha[95:101]
    MPRVALORMOV = linha[101:114]
    MPRVALORMOVCOMIS = linha[114:127]
    MPRCODCORRET = linha[127:132]
    MPRVALORMOVCORRET = linha[132:145]
    MPRVIGMED = linha[145:147]
    MPRBASEIND = linha[147:148]
    MPRMOEDA = linha[148:151]
    MPRTAXACONV = linha[151:164]
    MPRDATAEMISS = linha[164:172]
    
    # Verifica se não há linhas em branco
    try:
        if linha == "" or linha is None:
            conn.execute(make_command("T1", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T1", nome_arquivo, n, "409"))
    # Verifica o tamanho padrão da linha (deve conter 172 caracteres)
    try:
        if len(linha) != 172:
            conn.execute(make_command("T2", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T2", nome_arquivo, n, "409"))
    # Verifica se o campo sequencial MPRSEQ é uma sequência válida, que se
    # inicia em 0000001
    try:
        if int(linha[0:7]) != n:
            conn.execute(make_command("T3", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T3", nome_arquivo, n, "409"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    try:
        if linha[7:12] != entcodigo:
            conn.execute(make_command("T4", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T4", nome_arquivo, n, "409"))
    # Verifica se o campo MRFMESANO corresponde a um ano e mês válidos
    try:
        ciso8601.parse_datetime(linha[12:18] + "01")
    except ValueError:
        conn.execute(make_command("T5", nome_arquivo, n, "409"))
    # Verifica se o campo TPMORESSID corresponde a um tipo de movimento válido
    # (conforme tabela 'TiposMovimentosResseguros' do FIPSUSEP)
    try:
        if linha[18:21] not in ["035", "036", "037", "038",
                                "039", "040", "041", "042", "043", "044", "045"]:
            conn.execute(make_command("T6", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T6", nome_arquivo, n, "409"))
    # Verifica se o campo GRACODIGO corresponde a um grupo de ramos válido
    # operado pelo ressegurador
    try:
        if linha[21:23] not in gracodigos:
            conn.execute(make_command("T7", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T7", nome_arquivo, n, "409"))
    # Verifica se o campo MPRTIPOCONT foi preenchido com um tipo de contrato
    # válido
    try:
        if linha[60] not in ["1", "2"]:
            conn.execute(make_command("T8", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T8", nome_arquivo, n, "409"))
    # Verifica se o campo MPRMODCONT foi preenchido com uma modalidade de
    # contrato válida, exceto nos casos em que o tipo de contrato seja
    # ‘Facultativo’, quando o campo deve ser preenchido com ‘99’
    try:
        if (linha[61:63] not in ["01", "02", "03", "04", "05", "06"]) or (
                linha[60] == "2" and linha[61:63] != "99"):
            conn.execute(make_command("T9", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T9", nome_arquivo, n, "409"))
    # Para o tipo de contrato 'Facultativo', verifica se o tipo de movimento é
    # 'Emissão de Prêmio Efetivo' ou 'Endosso de Prêmio Efetivo' ou
    # 'Restituição de Prêmio Efetivo' ou 'Cancelamento de Prêmio Efetivo' ou
    # 'Informação sem Movimentação de Prêmio'
    try:
        if linha[60] == "2" and linha[18:21] not in ["35", "36", "37", "45"]:
            conn.execute(make_command("T10", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T10", nome_arquivo, n, "409"))
    # Para o tipo de contrato 'Automático' e para as modalidades de contrato
    # 'Proporcional', verifica se o tipo de movimento é 'Emissão de Prêmio
    # Efetivo' ou 'Endosso de Prêmio Efetivo' ou 'Restituição de Prêmio
    # Efetivo' ou 'Cancelamento de Prêmio Efetivo' ou 'Ajuste de Prêmio
    # Efetivo' ou 'Emissão de Prêmio Estimado' ou 'Alteração de Prêmio
    # Estimado' ou 'Cancelamento de Prêmio Estimado' ou 'Ajuste de Prêmio
    # Estimado' ou 'Informação sem Movimentação de Prêmio'
    pass
    # Para o tipo de contrato 'Automático' e para as modalidades de contrato
    # 'Não Proporcional' e 'Clash', verifica se o tipo de movimento é 'Emissão
    # de Prêmio Efetivo' ou 'Endosso de Prêmio Efetivo' ou 'Restituição de
    # Prêmio Efetivo' ou 'Cancelamento de Prêmio Efetivo' ou ' Ajuste de
    # Prêmio Efetivo' ou 'Prêmio de Reintegração' ou 'Informação sem
    # Movimentação de Prêmio'
    pass
    # Verifica se os campos MPRDATACEITE, MPRDATAINICIO, MPRDATAFIM e
    # MPRDATAEMISS correspondem a uma data válida
    try:
        ciso8601.parse_datetime(linha[63:71])
        ciso8601.parse_datetime(linha[79:87])
        ciso8601.parse_datetime(linha[87:95])
        ciso8601.parse_datetime(linha[164:172])
    except ValueError:
        conn.execute(make_command("T13", nome_arquivo, n, "409"))
    # Verifica se o campo MPRDATACONTR foi preenchido com uma data válida ou
    # com '99999999'
    try:
        if linha[71:79] != "99999999":
            try:
                ciso8601.parse_datetime(linha[71:79])
            except BaseException:
                conn.execute(make_command("T14", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T14", nome_arquivo, n, "409"))
    # Verifica se o valor dos campos MPRVALORMOV, MPRVALORMOVCOMISS,
    # MPRVALORMOVCORRET e MPRTAXACONV é float
    try:
        float(linha[101:114].replace(",", "."))
        float(linha[114:127].replace(",", "."))
        float(linha[127:132].replace(",", "."))
        float(linha[151:164].replace(",", "."))
    except ValueError:
        pass
    # Verifica se o campo MPRPERCRISCO corresponde a um valor entre '000,01' e
    # '100,00'
    try:
        if (0.01 <= float(linha[95:101].replace(",", ".")) <= 100) == False:
            conn.execute(make_command("T15", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T15", nome_arquivo, n, "409"))
    # Verifica se o campo MPRCODCORRET corresponde a um código de corretora de
    # resseguro válido  ou '99999'
    pass
    # Verifica se o campo MPRVIGMED corresponde a um valor entre '01' e '99'
    try:
        if (1 <= int(linha[145:147]) <= 99) == False:
            conn.execute(make_command("T17", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T17", nome_arquivo, n, "409"))
    # Verifica se o campo MPRBASEIND foi preenchido com uma base indenitária
    # válida
    try:
        if linha[147] not in ["1", "2", "3"]:
            conn.execute(make_command("T18", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T18", nome_arquivo, n, "409"))
    # Verifica se o campo MPRMOEDA foi preenchido com uma moeda válida
    try:
        if linha[148:151] not in moedas:
            conn.execute(make_command("T20", nome_arquivo, n, "409"))
    except:
        conn.execute(make_command("T20", nome_arquivo, n, "409"))