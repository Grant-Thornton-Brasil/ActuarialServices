import pandas as pd
import calendar
from datetime import datetime


# RESEGUROS
class maths_405():

    def __init__(self, dates):
        self.df = pd.DataFrame(index=dates, columns=[
            f"Cruzamento {i} - 405" for i in range(1, 6)])
        self.df.fillna(0.0, inplace=True)

    def run(self, linha):
        # Cruzamento 1
        # TPMORESSID 12+14-19+21 ; MSRTIPOSIN 1 ; MSRVALORMOV ; CMPID 12258
        if (linha[18:21] in ["012", "014", "021"]) and linha[112] == "1":
            self.df["Cruzamento 1 - 405"][linha[12:18]] \
                += float(linha[99:112])
        if (linha[18:21] == "019") and linha[112] == "1":
            self.df["Cruzamento 1 - 405"][linha[12:18]] \
                -= float(linha[99:112])
        # Cruzamento 2
        # TPMORESSID 12+14-19+21 ; MSRTIPOSIN 2 ; MSRVALORMOV ; CMPID 12259
        if linha[18:21] in ["012", "014", "021"] and linha[112] == "2":
            self.df["Cruzamento 1 - 405"][linha[12:18]] \
                += float(linha[99:112])
        if linha[18:21] == "019" and linha[112] == "2":
            self.df["Cruzamento 1 - 405"][linha[12:18]] \
                -= float(linha[99:112])
        # Cruzamento 3
        # TPMORESSID 13+15-20+22 ; MSRTIPOSIN 1 ; MSRVALORMOV ; CMPID 12262
        if linha[18:21] in ["013", "015", "020"] and linha[112] == "1":
            self.df["Cruzamento 3 - 405"][linha[12:18]] \
                += float(linha[99:112])
        if linha[18:21] == "020" and linha[112] == "1":
            self.df["Cruzamento 3 - 405"][linha[12:18]] \
                -= float(linha[99:112])
        # Cruzamento 4
        # TPMORESSID 13+15-20+22 ; MSRTIPOSIN 2 ; MSRVALORMOV ; CMPID 12263
        if linha[18:21] in ["013", "015", "020"] and linha[112] == "2":
            self.df["Cruzamento 4 - 405"][linha[12:18]] \
                += float(linha[99:112])
        if linha[18:21] == "020" and linha[112] == "2":
            self.df["Cruzamento 4 - 405"][linha[12:18]] \
                -= float(linha[99:112])
        # Cruzamento 5
        # TPMORESSID 14-19+21 ; MSRTIPOSIN 1+2 ; MSRVALORMOV ; CMPID 12273
        if linha[18:21] in ["014", "021"] and linha[112] in ["1", "2"]:
            self.df["Cruzamento 4 - 405"][linha[12:18]] \
                += float(linha[99:112])
        if linha[18:21] == "019" and linha[112] in ["1", "2"]:
            self.df["Cruzamento 4 - 405"][linha[12:18]] \
                -= float(linha[99:112])