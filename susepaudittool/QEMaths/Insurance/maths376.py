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
        # Cruzamento 1
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1001":
            self.df["Cruzamento 1 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1001":
            self.df["Cruzamento 1 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 2
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1002":
            self.df["Cruzamento 2 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1002":
            self.df["Cruzamento 2 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 3
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1003":
            self.df["Cruzamento 3 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1003":
            self.df["Cruzamento 3 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 4
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1006":
            self.df["Cruzamento 4 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1006":
            self.df["Cruzamento 4 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 5
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1007":
            self.df["Cruzamento 5 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1007":
            self.df["Cruzamento 5 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 6
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1008":
            self.df["Cruzamento 6 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1008":
            self.df["Cruzamento 6 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 7
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1012":
            self.df["Cruzamento 7 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1012":
            self.df["Cruzamento 7 - 376"][linha[12:20]] -= float(linha[67:80])
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1011":
            self.df["Cruzamento 7 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1011":
            self.df["Cruzamento 7 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 8
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1013":
            self.df["Cruzamento 8 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1013":
            self.df["Cruzamento 8 - 376"][linha[12:20]] -= float(linha[67:80])
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1014":
            self.df["Cruzamento 8 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1014":
            self.df["Cruzamento 8 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 9
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1004":
            self.df["Cruzamento 9 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1004":
            self.df["Cruzamento 9 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 10
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1009":
            self.df["Cruzamento 10 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1009":
            self.df["Cruzamento 10 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 11
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1005":
            self.df["Cruzamento 11 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1005":
            self.df["Cruzamento 11 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 12
        if linha[23:27] in ["0001", "0002", "0006"] and linha[27:31] == "1010":
            self.df["Cruzamento 12 - 376"][linha[12:20]] += float(linha[67:80])
        if linha[23:27] == "0005" and linha[27:31] == "1010":
            self.df["Cruzamento 12 - 376"][linha[12:20]] -= float(linha[67:80])
        # Cruzamento 13
            self.df["Cruzamento 13 - 376"] = self.df["Cruzamento 1 - 376"] + \
                self.df["Cruzamento 2 - 376"] - self.df["Cruzamento 3 - 376"] \
                + self.df["Cruzamento 4 - 376"] \
                + self.df["Cruzamento 5 - 376"] - self.df["Cruzamento 6 - 376"]
        # Cruzamento 14 - 1012 (+) 1011 (+) 1013 (+) 1014
        self.df["Cruzamento 14 - 376"] = self.df["Cruzamento 7 - 376"] \
            + self.df["Cruzamento 8 - 376"]