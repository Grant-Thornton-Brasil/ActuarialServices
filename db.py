def make_report(qe_type,conn,path):
    header = "File Name, Line, "
    command = 'SELECT "File Name", "Line", '
    if qe_type == 376:
        for column in range(1,14+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 377:
        for column in range(1,11+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 378:
        for column in range(1,13+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 404:
        for column in range(1,16+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 405:
        for column in range(1,13+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 406:
        for column in range(1,15+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 407:
        for column in range(1,12+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 408:
        for column in range(1,22+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 409:
        for column in range(1,23+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 419:
        for column in range(1,30+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 420:
        for column in range(1,15+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 421:
        for column in range(1,13+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 422:
        for column in range(1,12+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    elif qe_type == 423:
        for column in range(1,10+1):
            command += f"sum(T{column}), "
            header += f"T{column}, "
    
    command = command[:-2]+f' FROM "{qe_type}" GROUP BY "File Name", "Line";'
    query = conn.execute(command).fetchall()
    if len(query)==0:
        return
    with open(path+"\\detailed_export.csv","a+") as csv:
        csv.write(header+"\n")
        for row in query:
            csv.write(str(row).replace("(","").replace(")","").replace("'","")+"\n")


def create_main_tables(conn):
    QEs = [376, 377, 378, 404, 405, 406, 407, 408, 409,
       419, 420, 421, 422, 423]
    crits = [14, 11, 13,
            16, 13, 15, 12, 22, 23,
            30, 15, 13, 12, 10]
    for qe, crit in zip(QEs, crits):
        query = f'CREATE TABLE IF NOT EXISTS "{qe}" ("File Name" TEXT, Line INTEGER, '
        for n in range(1, crit + 1):
            query += f"T{n} INTEGER, "
        query = query[:-2] + ");"
        conn.execute(query)
