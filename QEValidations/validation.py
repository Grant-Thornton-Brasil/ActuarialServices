from .Capitalization.vali419 import validate_419
from .Capitalization.vali420 import validate_420
from .Capitalization.vali421 import validate_421
from .Capitalization.vali422 import validate_422
from .Capitalization.vali423 import validate_423
from .Insurance.vali376 import validate_376
from .Insurance.vali377 import validate_377
from .Insurance.vali378 import validate_378
from .Reinsurance.vali404 import validate_404
from .Reinsurance.vali405 import validate_405
from .Reinsurance.vali406 import validate_406
from .Reinsurance.vali407 import validate_407
from .Reinsurance.vali408 import validate_408
from .Reinsurance.vali409 import validate_409
import calendar
from datetime import datetime


def run_validations(**kwargs):
    """
    Kwargs:
        qe (str): Quadro Estatístico
        nome_arquivo (str): Nome do Arquivo
        linha (str): Linha do Arquivo
        n (int): Número da Linha do Arquivo
        conn (Connection): Conexão SLQLITE3
        year (int): Datas
        entcodigo (list):
        ramcodigos (list):
        esrcodcess (list):
    """
    qe = kwargs.get("QE")
    nome_arquivo = kwargs.get("nome_arquivo")
    linha = kwargs.get("linha")
    n = kwargs.get("n")
    conn = kwargs.get("conn")
    year = kwargs.get("year")
    entcodigo = kwargs.get("entcodigo")
    ramcodigos = kwargs.get("ramcodigos")
    esrcodcess = kwargs.get("esrcodcess")
    gracodigos = kwargs.get("gracodigos")

    dates_seguros = [datetime(year, month, calendar.monthrange(year, month)[
    1]).strftime("%Y%m%d") for month in range(1, 13)]
    dates_reseguros = [f"2018" + f"{month}".zfill(2) for month in range(1, 13)]

    # SEGUROS
    if qe == "376" or 376:
        validate_376(
            nome_arquivo,
            linha,
            n,
            conn,
            dates_seguros,
            entcodigo,
            ramcodigos,
            esrcodcess
        )
    elif qe == "377" or 377:
        validate_377(
            nome_arquivo,
            linha,
            n,
            conn,
            dates_seguros,
            entcodigo,
            ramcodigos,
            esrcodcess
        )
    elif qe == "378" or 378:
        validate_378(
            nome_arquivo,
            linha,
            n,
            conn,
            dates_seguros,
            entcodigo,
            ramcodigos,
            esrcodcess
        )
    # RESSEGUROS
    elif qe == "404" or 404:
        validate_404(
            nome_arquivo,
            linha,
            n,
            conn,
            dates,
            entcodigo,
            gracodigos
        )
    elif qe == "405" or 405:
        validate_405(
            nome_arquivo,
            linha,
            n,
            conn,
            dates,
            entcodigo,
            gracodigos
        )
    elif qe == "406" or 406:
        validate_406(
            nome_arquivo,
            linha,
            n,
            conn,
            dates,
            entcodigo,
            gracodigos
        )
    elif qe == "407" or 407:
        validate_407(
            nome_arquivo,
            linha,
            n,
            conn,
            dates,
            entcodigo,
            gracodigos
        )
    elif qe == "408" or 408:
        validate_408(
            nome_arquivo,
            linha,
            n,
            conn,
            dates,
            entcodigo,
            gracodigos
        )
    elif qe == "409" or 409:
        validate_409(
            nome_arquivo,
            linha,
            n,
            conn,
            dates,
            entcodigo,
            gracodigos
        )
    # CAPITALIZAÇÃO
