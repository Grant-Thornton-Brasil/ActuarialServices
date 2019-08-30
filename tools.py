import os
from tkinter import Tk
from tkinter import filedialog


def get_lines_from_txts():
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    arquivos = list(filedialog.askopenfilenames(
        filetypes=[("Arquivos TXT", "*.txt")]))
    for arquivo in arquivos:
        with open(arquivo) as txt:
            linhas = txt.readlines()
            for n, linha in enumerate(linhas, 1):
                yield [txt.name, linha.strip().replace(",", "."), n]


def get_moedas():
    moedas = []
    with open(os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "TXTs", "moedas.txt")), "r") as txt:
        for linha in txt.readlines():
            moedas.append(linha.strip())
    return moedas


def get_ramos():
    ramos = []
    with open(os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "TXTs", "ramos.txt")), "r", encoding="utf8") as txt:
        for linha in txt.readlines():
            ramos.append(linha.strip())
    return ramos
