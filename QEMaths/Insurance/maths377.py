import pandas as pd
import calendar
from datetime import datetime


# SEGUROS
class maths_377():

    def __init__(self, dates):
        self.df = pd.DataFrame(index=dates, columns=[
                               f"Cruzamento {i} - 377" for i in range(1, 11)])
        self.df.fillna(0.0, inplace=True)

    def run(self, linha):
        # Cruzamento 1
        if int(linha[23:27]) == 1015:
            self.df["Cruzamento 1 - 377"][linha[12:20]] += float(linha[63:76])
        # Cruzamento 2
        if int(linha[23:27]) == 1016:
            self.df["Cruzamento 2 - 377"][linha[12:20]] += float(linha[63:76])
        # Cruzamento 3
        if int(linha[23:27]) == 1017:
            self.df["Cruzamento 3 - 377"][linha[12:20]] += float(linha[63:76])
        # Cruzamento 4
        if int(linha[23:27]) == 1018:
            self.df["Cruzamento 4 - 377"][linha[12:20]] += float(linha[63:76])
        # Cruzamento 5
        if int(linha[23:27]) == 1020:
            self.df["Cruzamento 5 - 377"][linha[12:20]] += float(linha[63:76])
        # Cruzamento 6
        if int(linha[23:27]) == 1021:
            self.df["Cruzamento 6 - 377"][linha[12:20]] += float(linha[63:76])
        # Cruzamento 7
        if int(linha[23:27]) == 1022:
            self.df["Cruzamento 7 - 377"][linha[12:20]] += float(linha[63:76])
        # Cruzamento 8
        if int(linha[23:27]) == 1023:
            self.df["Cruzamento 8 - 377"][linha[12:20]] += float(linha[63:76])
        # Cruzamento 9
        if int(linha[23:27]) == 1019:
            self.df["Cruzamento 9 - 377"][linha[12:20]] += float(linha[63:76])
        if int(linha[23:27]) == 1024:
            self.df["Cruzamento 9 - 377"][linha[12:20]] += float(linha[63:76])
        # Cruzamento 10
        if int(linha[23:27]) == 1025:
            self.df["Cruzamento 10 - 377"][linha[12:20]] += float(linha[63:76])