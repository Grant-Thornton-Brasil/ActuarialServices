import pandas as pd
import calendar
from datetime import datetime


# SEGUROS
class maths_376():

    def __init__(self, dates):
        self.df = pd.DataFrame(index=dates, columns=[
                               f"Cruzamento {i} - 376" for i in range(1, 15)])
        self.df.fillna(0.0, inplace=True)

    def run(self, linha):
        # VARS
        MRFMESANO = linha[12:20]
        TPMOID = linha[23:27]
        CMPID = linha[27:31]
        ESRVALORMOV = float(linha[67:80])

        # Cruzamento 1
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1001":
            self.df["Cruzamento 1 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1001":
            self.df["Cruzamento 1 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 2
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1002":
            self.df["Cruzamento 2 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1002":
            self.df["Cruzamento 2 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 3
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1003":
            self.df["Cruzamento 3 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1003":
            self.df["Cruzamento 3 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 4
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1006":
            self.df["Cruzamento 4 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1006":
            self.df["Cruzamento 4 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 5
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1007":
            self.df["Cruzamento 5 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1007":
            self.df["Cruzamento 5 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 6
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1008":
            self.df["Cruzamento 6 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1008":
            self.df["Cruzamento 6 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 7
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1012":
            self.df["Cruzamento 7 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1012":
            self.df["Cruzamento 7 - 376"][MRFMESANO] -= ESRVALORMOV
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1011":
            self.df["Cruzamento 7 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1011":
            self.df["Cruzamento 7 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 8
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1013":
            self.df["Cruzamento 8 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1013":
            self.df["Cruzamento 8 - 376"][MRFMESANO] -= ESRVALORMOV
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1014":
            self.df["Cruzamento 8 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1014":
            self.df["Cruzamento 8 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 9
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1004":
            self.df["Cruzamento 9 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1004":
            self.df["Cruzamento 9 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 10
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1009":
            self.df["Cruzamento 10 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1009":
            self.df["Cruzamento 10 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 11
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1005":
            self.df["Cruzamento 11 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1005":
            self.df["Cruzamento 11 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 12
        if TPMOID in ["0001", "0002", "0006"] and CMPID == "1010":
            self.df["Cruzamento 12 - 376"][MRFMESANO] += ESRVALORMOV
        if TPMOID == "0005" and CMPID == "1010":
            self.df["Cruzamento 12 - 376"][MRFMESANO] -= ESRVALORMOV
        # Cruzamento 13
            self.df["Cruzamento 13 - 376"] = self.df["Cruzamento 1 - 376"] + \
                self.df["Cruzamento 2 - 376"] - self.df["Cruzamento 3 - 376"] \
                + self.df["Cruzamento 4 - 376"] \
                + self.df["Cruzamento 5 - 376"] - self.df["Cruzamento 6 - 376"]
        # Cruzamento 14 - 1012 (+) 1011 (+) 1013 (+) 1014
        self.df["Cruzamento 14 - 376"] = self.df["Cruzamento 7 - 376"] \
            + self.df["Cruzamento 8 - 376"]