import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import *

moedas = get_moedas()


# RESEGUROS
def validate_405(nome_arquivo, linha, n, conn, dates,
                 entcodigo, gracodigos):
    MSRSEQ = linha[0:7]
    ENTCODIGO = linha[7:12]
    MRFMESANO = linha[12:18]
    TPMORESSID = linha[18:21]
    GRACODIGO = linha[21:23]
    MSRVALORMOV = linha[99:112]
    MSRTIPOSIN = linha[112:113]
    MSRMODCONT = linha[113:115]
    MSRMOEDA = linha[115:118]
    MSRBASEIND = linha[118:119]
    MSRVALORMON = linha[119:132]

    # 1	Verifica se não há linhas em branco
    try:
        if linha == "" or linha is None:
            conn.execute(make_command("T1", nome_arquivo, n, "405"))
    except:
        conn.execute(make_command("T1", nome_arquivo, n, "405"))
    # 2	Verifica o tamanho padrão da linha (deve conter 132 caracteres)
    try:
        if len(linha) != 132:
            conn.execute(make_command("T2", nome_arquivo, n, "405"))
    except:
        conn.execute(make_command("T2", nome_arquivo, n, "405"))
    # 3 Verifica se o campo sequencial MSRSEQ é uma sequência válida,
    # que se inicia em 0000001
    try:
        if int(MSRSEQ) != n:
            conn.execute(make_command("T3", nome_arquivo, n, "405"))
    except:
        conn.execute(make_command("T3", nome_arquivo, n, "405"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    try:
        if ENTCODIGO != entcodigo:
            conn.execute(make_command("T4", nome_arquivo, n, "405"))
    except:
        conn.execute(make_command("T4", nome_arquivo, n, "405"))
    # Verifica se o campo MRFMESANO corresponde a um ano e mês válidos
    try:
        ciso8601.parse_datetime(MRFMESANO + "01")
    except ValueError:
        conn.execute(make_command("T5", nome_arquivo, n, "405"))
    # Verifica se o campo TPMORESSID corresponde a um tipo de movimento válido
    # (conforme tabela 'TiposMovimentosResseguros' do FIPSUSEP)
    try:
        if TPMORESSID not in ["012", "013", "014", "015", "016", "017",
                                "018", "019", "020", "021", "022", "023"]:
            conn.execute(make_command("T6", nome_arquivo, n, "405"))
    except:
        conn.execute(make_command("T6", nome_arquivo, n, "405"))
    # Verifica se o campo GRACODIGO corresponde a um grupo de ramos válido
    # operado pelo ressegurador
    try:
        if GRACODIGO not in gracodigos:
            conn.execute(make_command("T7", nome_arquivo, n, "405"))
    except:
        conn.execute(make_command("T7", nome_arquivo, n, "405"))
    # Verifica se o campo MSRTIPOCONT foi preenchido com um tipo de contrato
    # válido
    try:
        if linha[69] not in ["1", "2"]:
            conn.execute(make_command("T8", nome_arquivo, n, "405"))
    except:
        conn.execute(make_command("T8", nome_arquivo, n, "405"))
    # Verifica se o valor dos campos MSRVALORMOV e MSRVALORMON é float
    try:
        float(MSRVALORMOV)
        float(MSRVALORMON)
    except ValueError:
        conn.execute(make_command("T9", nome_arquivo, n, "405"))
    # Verifica se o campo MSRTIPOSIN foi preenchido com um tipo de sinistro
    # válido
    try:
        if MSRTIPOSIN not in ["1", "2", "3", "4"]:
            conn.execute(make_command("T10", nome_arquivo, n, "405"))
    except:
        conn.execute(make_command("T10", nome_arquivo, n, "405"))
    # Verifica se o campo MSRMODCONT foi preenchido com uma modalidade de
    # contrato válida, exceto nos casos em que o tipo de contrato seja
    # ‘Facultativo’, quando o campo deve ser preenchido com ‘99’
    try:
        if MSRMODCONT not in ["1", "2", "3", "4", "5", "6"] or (
                linha[69] == "2" and MSRMODCONT != "99"):
            conn.execute(make_command("T11", nome_arquivo, n, "404"))
    except:
        conn.execute(make_command("T11", nome_arquivo, n, "404"))
    # Verifica se o campo MSRMOEDA foi preenchido com uma moeda válida
    try:
        if MSRMOEDA not in moedas:
            conn.execute(make_command("T12", nome_arquivo, n, "405"))
    except:
        conn.execute(make_command("T12", nome_arquivo, n, "405"))
    # Verifica se o campo MSRBASEIND foi preenchido com uma base indenitária
    # válida
    try:
        if MSRBASEIND not in ["1", "2", "3"]:
            conn.execute(make_command("T13", nome_arquivo, n, "405"))
    except:
        conn.execute(make_command("T13", nome_arquivo, n, "405"))