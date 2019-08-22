# TOOLS
def make_command(column, nome_arquivo, n, QE):
    command = 'INSERT INTO "QE" ("File Name", "Line", TX) \
        VALUES ("filex", linex, 1);'

    return command.replace("TX", column).replace(
        "filex", nome_arquivo).replace("linex", str(n)).replace("QE", QE)