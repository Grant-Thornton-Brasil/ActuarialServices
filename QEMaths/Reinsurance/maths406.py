import pandas as pd
import calendar
from datetime import datetime


# RESEGUROS
class maths_406():

    def __init__(self, dates):
        self.df = pd.DataFrame(index=dates, columns=[
            f"Cruzamento {i} - 406" for i in range(1, 6)])
        self.df.fillna(0.0, inplace=True)

    def run(self, linha):
        # Cruzamento 1
        # SLATIPOPERA 1 ; SLATIPOSIN 1 ; SLAVALORMOVPEN ; CMPID 12338
        if linha[18] == "1" and linha[124] == "1":
            self.df["Cruzamento 1 - 406"][linha[12:18]] \
                += float(linha[110:123])
        # Cruzamento 2
        # SLATIPOPERA 1 ; SLATIPOSIN 2 ; SLAVALORMOVPEN ; CMPID 12339
        if linha[18] == "1" and linha[124] == "2":
            self.df["Cruzamento 2 - 406"][linha[12:18]] \
                += float(linha[110:123])
        # Cruzamento 3
        # SLATIPOPERA 2 ; SLATIPOSIN 1 ; SLAVALORMOVPEN ; CMPID 12341
        if linha[18] == "2" and linha[124] == "1":
            self.df["Cruzamento 3 - 406"][linha[12:18]] \
                += float(linha[110:123])
        # Cruzamento 4
        # SLATIPOPERA 2 ; SLATIPOSIN 2 ; SLAVALORMOVPEN ; CMPID 12342
        if linha[18] == "2" and linha[124] == "2":
            self.df["Cruzamento 4 - 406"][linha[12:18]] \
                += float(linha[110:123])