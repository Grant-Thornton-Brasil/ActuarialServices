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
        # VARS
        MRFMESANO = linha[12:20]
        CMPID = linha[23:27]
        ESLVALORMOV = float(linha[63:76])

        # Cruzamento 1
        if CMPID == "1015":
            self.df["Cruzamento 1 - 377"][MRFMESANO] += ESLVALORMOV
        # Cruzamento 2
        if CMPID == "1016":
            self.df["Cruzamento 2 - 377"][MRFMESANO] += ESLVALORMOV
        # Cruzamento 3
        if CMPID == "1017":
            self.df["Cruzamento 3 - 377"][MRFMESANO] += ESLVALORMOV
        # Cruzamento 4
        if CMPID == "1018":
            self.df["Cruzamento 4 - 377"][MRFMESANO] += ESLVALORMOV
        # Cruzamento 5
        if CMPID == "1020":
            self.df["Cruzamento 5 - 377"][MRFMESANO] += ESLVALORMOV
        # Cruzamento 6
        if CMPID == "1021":
            self.df["Cruzamento 6 - 377"][MRFMESANO] += ESLVALORMOV
        # Cruzamento 7
        if CMPID == "1022":
            self.df["Cruzamento 7 - 377"][MRFMESANO] += ESLVALORMOV
        # Cruzamento 8
        if CMPID == "1023":
            self.df["Cruzamento 8 - 377"][MRFMESANO] += ESLVALORMOV
        # Cruzamento 9
        if CMPID == "1019":
            self.df["Cruzamento 9 - 377"][MRFMESANO] += ESLVALORMOV
        if CMPID == "1024":
            self.df["Cruzamento 9 - 377"][MRFMESANO] += ESLVALORMOV
        # Cruzamento 10
        if CMPID == "1025":
            self.df["Cruzamento 10 - 377"][MRFMESANO] += ESLVALORMOV