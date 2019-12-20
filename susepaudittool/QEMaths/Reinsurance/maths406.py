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
        MRFMESANO = linha[12:18]
        SLATIPOPERA = linha[20:21]
        SLAVALORMOVPEN = linha[97:110]
        SLATIPOSIN = linha[123:124]
        # Cruzamento 1
        # SLATIPOPERA 1 ; SLATIPOSIN 1 ; SLAVALORMOVPEN ; CMPID 12338
        if SLATIPOPERA == "1" and SLATIPOSIN == "1":
            self.df["Cruzamento 1 - 406"][MRFMESANO] += float(SLAVALORMOVPEN)
        # Cruzamento 2
        # SLATIPOPERA 1 ; SLATIPOSIN 2 ; SLAVALORMOVPEN ; CMPID 12339
        elif SLATIPOPERA == "1" and SLATIPOSIN == "2":
            self.df["Cruzamento 2 - 406"][MRFMESANO] += float(SLAVALORMOVPEN)
        # Cruzamento 3
        # SLATIPOPERA 2 ; SLATIPOSIN 1 ; SLAVALORMOVPEN ; CMPID 12341
        elif SLATIPOPERA == "2" and SLATIPOSIN == "1":
            self.df["Cruzamento 3 - 406"][MRFMESANO] += float(SLAVALORMOVPEN)
        # Cruzamento 4
        # SLATIPOPERA 2 ; SLATIPOSIN 2 ; SLAVALORMOVPEN ; CMPID 12342
        elif SLATIPOPERA == "2" and SLATIPOSIN == "2":
            self.df["Cruzamento 4 - 406"][MRFMESANO] += float(SLAVALORMOVPEN)