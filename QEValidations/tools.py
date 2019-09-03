import os

# TOOLS
def make_command(column, nome_arquivo, n, QE):
    command = 'INSERT INTO "QE" ("File Name", "Line", TX) \
        VALUES ("filex", linex, 1);'

    return command.replace("TX", column).replace(
        "filex", nome_arquivo).replace("linex", str(n)).replace("QE", QE)
    
def get_moedas():
    moedas = []
    with open(os.path.abspath(os.path.join("TXTs", "moedas.txt"))) as txt:
        for linha in txt.readlines():
            moedas.append(linha.strip())
    return moedas


def get_ramos():
    ramos = []
    with open(os.path.abspath(os.path.join("TXTs", "ramos.txt"))) as txt:
        for linha in txt.readlines():
            ramos.append(linha.strip())
    return ramos