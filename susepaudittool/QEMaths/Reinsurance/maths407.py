import pandas as pd
import calendar
from datetime import datetime


# RESEGUROS
class maths_407():

    def __init__(self, dates):
        self.df = pd.DataFrame(index=dates, columns=[
            f"Cruzamento {i} - 407" for i in range(1, 4)])
        self.df.fillna(0.0, inplace=True)

    def run(self, linha):
        # Cruzamento 1
        # SLATIPOSIN 1 ; SLRVALORMOVPEN ; CMPID 12352
        if linha[122] == "1":
            self.df["Cruzamento 1 - 407"][linha[12:18]] \
                += float(linha[96:109])
        # Cruzamento 2
        # SLATIPOSIN 2 ; SLRVALORMOVPEN ; CMPID 12353
        if linha[122] == "2":
            self.df["Cruzamento 2 - 407"][linha[12:18]] \
                += float(linha[96:109])
        # Cruzamento 3
        # SLATIPOSIN 3+4 ; SLRVALORMOVPEN ; CMPID 12379
        if linha[122] in ["3", "4"]:
            self.df["Cruzamento 3 - 407"][linha[12:18]] \
                += float(linha[96:109])