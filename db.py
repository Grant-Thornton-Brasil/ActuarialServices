QEs = [376, 377, 378, 404, 405, 406, 407, 408, 409,
       419, 420, 421, 422, 423]
crits = [14, 11, 13,
         16, 13, 15, 12, 22, 23,
         30, 15, 13, 12, 10]


def make_report(qe_type, conn, path):
    for qe, crit in zip(QEs, crits):
        counter = conn.execute(f'SELECT count(*) FROM "{qe}";')
        if counter.fetchone()[0] != 0:
            with open(path + f"\\export_detailed_{qe}.csv", "a+") as csv:
                query = conn.execute(f'SELECT * FROM "{qe}"')
                header = "Caminho, Número Linha,"
                for n in range(1, crit + 1):
                    header += f" Crítica {n},"
                header = header[:-1] + ";"
                csv.write(header + "\n")
                for linha in query:
                    csv.write(
                        str(linha).replace(
                            "(",
                            "").replace(
                            ")",
                            "").replace(
                            "None",
                            "") + "\n")


def create_main_tables(conn):

    for qe, crit in zip(QEs, crits):
        query = f'CREATE TABLE IF NOT EXISTS "{qe}" ("File Name" TEXT, Line INTEGER, '
        for n in range(1, crit + 1):
            query += f"T{n} INTEGER, "
        query = query[:-2] + ");"
        conn.execute(query)
