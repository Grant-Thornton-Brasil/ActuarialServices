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
        MRFMESANO = linha[12:18]
        TPMORESSID = linha[18:21]
        MSATIPOPERA = linha[23:24]
        MSAVALORMOV = linha[100:113]
        MSATIPOSIN = linha[113:114]
        # Cruzamento 1
        # TPMORESSID 1+3-8+10 ; MSATIPOPERA 1 ; MSATIPOSIN 1 ; MSAVALORMOV ;
        if MSATIPOPERA == "1" and MSATIPOSIN == "1":
            if TPMORESSID in ["001", "003", "010"]:
                self.df["Cruzamento 1 - 404"][MRFMESANO] += float(MSAVALORMOV) 
            elif TPMORESSID == "008":
                self.df["Cruzamento 1 - 404"][MRFMESANO] -= float(MSAVALORMOV) 
        # Cruzamento 2
        # TPMORESSID 1+3-8+10 ; MSATIPOPERA 1 ; MSATIPOSIN 2 ; MSAVALORMOV ;
        # CMPID 12245
        if MSATIPOPERA == "1" and MSATIPOSIN == "2":
            if TPMORESSID in ["001", "003", "010"]:
                self.df["Cruzamento 2 - 404"][MRFMESANO] += float(MSAVALORMOV) 
            elif TPMORESSID == "008":
                self.df["Cruzamento 2 - 404"][MRFMESANO] -= float(MSAVALORMOV) 
        # Cruzamento 3
        # TPMORESSID 1+3-8+10 ; MSATIPOPERA 2 ; MSATIPOSIN 1+2 ; MSAVALORMOV ;
        # CMPID 12246
        if MSATIPOPERA == "2" and MSATIPOSIN in ["1","2"]:
            if TPMORESSID in ["001", "003", "010"]:
                self.df["Cruzamento 3 - 404"][MRFMESANO] += float(MSAVALORMOV)
            elif TPMORESSID == "008":
                self.df["Cruzamento 3 - 404"][MRFMESANO] -= float(MSAVALORMOV)
        # Cruzamento 4
        # TPMORESSID 2+4-9+11 ; MSATIPOPERA 1 ; MSATIPOSIN 1 ; MSAVALORMOV ;
        # CMPID 12249
        if MSATIPOPERA == "1" and MSATIPOSIN == "1":
            if TPMORESSID in ["002", "004", "011"]:
                self.df["Cruzamento 4 - 404"][MRFMESANO] += float(MSAVALORMOV)
            elif TPMORESSID == "009":
                self.df["Cruzamento 4 - 404"][MRFMESANO] -= float(MSAVALORMOV)
        # Cruzamento 5
        # TPMORESSID 2+4-9+11 ; MSATIPOPERA 1 ; MSATIPOSIN 2 ; MSAVALORMOV ;
        # CMPID 12250
        if MSATIPOPERA == "1" and MSATIPOSIN == "2":
            if TPMORESSID in ["002", "004", "011"]:
                self.df["Cruzamento 5 - 404"][MRFMESANO] += float(MSAVALORMOV)
            elif TPMORESSID == "009":
                self.df["Cruzamento 5 - 404"][MRFMESANO] -= float(MSAVALORMOV)
        # Cruzamento 6
        # TPMORESSID 2+4-9+11 ; MSATIPOPERA 2 ; MSATIPOSIN 1+2 ; MSAVALORMOV ;
        # CMPID 12251
        if MSATIPOPERA == "2" and MSATIPOSIN in ["1","2"]:
            if TPMORESSID in ["002", "004", "011"]:
                self.df["Cruzamento 6 - 404"][MRFMESANO] += float(MSAVALORMOV)
            elif TPMORESSID == "009":
                self.df["Cruzamento 6 - 404"][MRFMESANO] -= float(MSAVALORMOV)
        # Cruzamento 7
        # TPMORESSID 1+3-8+10 ; MSATIPOPERA 1+2 ; MSATIPOSIN 1+2 ; MSAVALORMON
        # CMPID 12272
        if MSATIPOPERA in ["1","2"] and MSATIPOSIN in ["1","2"]:
            if TPMORESSID in ["001", "003", "010"]:
                self.df["Cruzamento 7 - 404"][MRFMESANO] += float(MSAVALORMON)
            elif TPMORESSID == "008":
                self.df["Cruzamento 7 - 404"][MRFMESANO] -= float(MSAVALORMON)
