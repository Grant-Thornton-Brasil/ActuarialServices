import pandas as pd
import calendar
from datetime import datetime


# RESEGUROS
class maths_404():

    def __init__(self, dates):
        self.df = pd.DataFrame(index=dates, columns=[
            f"Cruzamento {i} - 404" for i in range(1, 8)])
        self.df.fillna(0.0, inplace=True)

    def run(self, linha):
        # Cruzamento 1
        # TPMORESSID 1+3-8+10 ; MSATIPOPERA 1 ; MSATIPOSIN 1 ; MSAVALORMOV ;
        # CMPID 12244
        if linha[18:21] in ["001", "003",
                            "010"] and linha[23] == "1" and linha[113] == "1":
            self.df["Cruzamento 1 - 404"][linha[12:18]] \
                += float(linha[100:113])
        if linha[18:21] == "008" and linha[23] == "1" and linha[113] == "1":
            self.df["Cruzamento 1 - 404"][linha[12:18]] \
                -= float(linha[100:113])
        # Cruzamento 2
        # TPMORESSID 1+3-8+10 ; MSATIPOPERA 1 ; MSATIPOSIN 2 ; MSAVALORMOV ;
        # CMPID 12245
        if linha[18:21] in ["001", "003",
                            "010"] and linha[23] == "1" and linha[113] == "2":
            self.df["Cruzamento 1 - 404"][linha[12:18]] \
                += float(linha[100:113])
        if linha[18:21] == "008" and linha[23] == "1" and linha[113] == "2":
            self.df["Cruzamento 1 - 404"][linha[12:18]] \
                -= float(linha[100:113])
        # Cruzamento 3
        # TPMORESSID 1+3-8+10 ; MSATIPOPERA 2 ; MSATIPOSIN 1+2 ; MSAVALORMOV ;
        # CMPID 12246
        if linha[18:21] in ["001", "003",
                            "010"] and linha[23] == "2" and linha[113] in ["1", "2"]:
            self.df["Cruzamento 3 - 404"][linha[12:18]] \
                += float(linha[100:113])
        if linha[18:21] == "010" and linha[23] == "2" and linha[113] in [
                "1", "2"]:
            self.df["Cruzamento 3 - 404"][linha[12:18]] \
                -= float(linha[100:113])
        # Cruzamento 4
        # TPMORESSID 2+4-9+11 ; MSATIPOPERA 1 ; MSATIPOSIN 1 ; MSAVALORMOV ;
        # CMPID 12249
        if linha[18:21] in ["002", "004",
                            "011"] and linha[23] == "1" and linha[113] == "1":
            self.df["Cruzamento 4 - 404"][linha[12:18]] \
                += float(linha[100:113])
        if linha[18:21] == "009" and linha[23] == "1" and linha[113] == "1":
            self.df["Cruzamento 4 - 404"][linha[12:18]] \
                -= float(linha[100:113])
        # Cruzamento 5
        # TPMORESSID 2+4-9+11 ; MSATIPOPERA 1 ; MSATIPOSIN 2 ; MSAVALORMOV ;
        # CMPID 12250
        if linha[18:21] in ["002", "004",
                            "011"] and linha[23] == "1" and linha[113] == "2":
            self.df["Cruzamento 5 - 404"][linha[12:18]] \
                += float(linha[100:113])
        if linha[18:21] == "009" and linha[23] == "1" and linha[113] == "2":
            self.df["Cruzamento 5 - 404"][linha[12:18]] \
                -= float(linha[100:113])
        # Cruzamento 6
        # TPMORESSID 2+4-9+11 ; MSATIPOPERA 1 ; MSATIPOSIN 2 ; MSAVALORMOV ;
        # CMPID 12251
        if linha[18:21] in ["002", "004",
                            "011"] and linha[23] == "1" and linha[113] == "2":
            self.df["Cruzamento 6 - 404"][linha[12:18]] \
                += float(linha[100:113])
        if linha[18:21] == "009" and linha[23] == "1" and linha[113] == "2":
            self.df["Cruzamento 6 - 404"][linha[12:18]] \
                -= float(linha[100:113])
        # Cruzamento 7
        # TPMORESSID 1+3-8+10 ; MSATIPOPERA 1+2 ; MSATIPOSIN 1+2 ; MSAVALORMON
        # ; CMPID 12272
        if linha[18:21] in ["001", "003", "010"] and linha[23] in [
                "1", "2"] and linha[113] in ["1", "2"]:
            self.df["Cruzamento 7 - 404"][linha[12:18]] \
                += float(linha[120:133])
        if linha[18:21] == "008" and linha[23] in [
                "1", "2"] and linha[113] in ["1", "2"]:
            self.df["Cruzamento 7 - 404"][linha[12:18]] \
                -= float(linha[120:133])