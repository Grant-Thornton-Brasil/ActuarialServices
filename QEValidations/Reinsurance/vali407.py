import ciso8601
from pycpfcnpj import cpfcnpj
from ..tools import make_command


# RESEGUROS
def validate_407(nome_arquivo, linha, n, conn, dates,
                 entcodigo, gracodigos):

    # Verifica se não há linhas em branco
    if linha == "" or linha is None:
        conn.execute(make_command("T1", nome_arquivo, n, "407"))
    # Verifica o tamanho padrão da linha (deve conter 129 caracteres)
    if len(linha) != 129:
        conn.execute(make_command("T2", nome_arquivo, n, "407"))
    # Verifica se o campo sequencial SLRSEQ é uma sequência válida, que se
    # inicia em 0000001
    if int(linha[0:7]) != n:
        conn.execute(make_command("T3", nome_arquivo, n, "407"))
    # Verifica se o campo ENTCODIGO corresponde à sociedade que está enviando
    # o FIP/SUSEP
    if linha[7:12] != entcodigo:
        conn.execute(make_command("T4", nome_arquivo, n, "407"))
    # Verifica se o campo MRFMESANO corresponde a um ano e mês válidos
    try:
        ciso8601.parse_datetime(linha[12:18] + "01")
    except ValueError:
        conn.execute(make_command("T5", nome_arquivo, n, "407"))
    # Verifica se o campo GRACODIGO corresponde a um grupo de ramos válido
    # operado pelo ressegurador
    if linha[18:20] not in gracodigos:
        conn.execute(make_command("T6", nome_arquivo, n, "407"))
    # Verifica se o campo SLRTIPOCONT foi preenchido com um tipo de contrato
    # válido
    if linha[66] not in ["1", "2"]:
        conn.execute(make_command("T7", nome_arquivo, n, "407"))
    # Verifica se o valor dos campos SLRVALORMOVPEN e SLRVALORMOVTOT é float
    try:
        float(linha[96:109])
        float(linha[109:122])
    except ValueError:
        conn.execute(make_command("T8", nome_arquivo, n, "407"))
    # Verifica se o campo SLRTIPOSIN foi preenchido com um tipo de sinistro
    # válido
    if linha[122:123] not in ["1", "2", "3", "4"]:
        conn.execute(make_command("T9", nome_arquivo, n, "407"))
    # Verifica se o campo SLRMODCONT foi preenchido com uma modalidade de
    # contrato válida, exceto nos casos em que o tipo de contrato seja
    # ‘Facultativo’, quando o campo deve ser preenchido com ‘99’
    if linha[124:126] not in ["01", "02", "03", "04", "05", "06"] and (
            linha[67] == "2" and linha[124:126] != "99"):
        conn.execute(make_command("T10", nome_arquivo, n, "407"))
    # Verifica se o campo SLRMOEDA foi preenchido com uma moeda válida
    if linha[125:128] not in moedas:
        conn.execute(make_command("T11", nome_arquivo, n, "407"))
    # Verifica se o campo SLRBASEIND foi preenchido com uma base indenitária
    # válida
    if linha[128] not in ["1", "2", "3"]:
        conn.execute(make_command("T12", nome_arquivo, n, "407"))