import pandas as pd
import calendar
from datetime import datetime


# SEGUROS
class maths_378():

    def __init__(self, dates):
        self.df = pd.DataFrame(index=dates, columns=[
            f"Cruzamento {i} - 378" for i in range(1, 17)])
        self.df.fillna(0.0, inplace=True)

    def run(self, linha):
        MRFMESANO = linha[12:20]
        TPMOID = int(linha[23:27])
        CMPID = int(linha[27:31])
        ESPVALORMOVRO = float(linha[59:72])
        ESPVALORMOVRD = float(linha[96:109])
        ESPVALORCARO = float(linha[118:131])
        ESPVALORCARD = float(linha[131:144])
        ESPVALORCIRO = float(linha[144:157])
        ESPVALORCIRD = float(linha[157:170])
        # Cruzamento 1
        if TPMOID == 7 and CMPID == 1026:
            self.df["Cruzamento 1 - 378"][MRFMESANO] += ESPVALORMOVRO - ESPVALORCIRO
        if TPMOID == 8 and CMPID == 1026:
            self.df["Cruzamento 1 - 378"][MRFMESANO] += ESPVALORMOVRD - ESPVALORCIRD
        # Cruzamento 2
        if TPMOID == 7 and CMPID == 1027:
            self.df["Cruzamento 2 - 378"][MRFMESANO] += ESPVALORMOVRO
        if TPMOID == 8 and CMPID == 1027:
            self.df["Cruzamento 2 - 378"][MRFMESANO] += ESPVALORMOVRD
        # Cruzamento 3
        if TPMOID == 7 and CMPID == 1028:
            self.df["Cruzamento 3 - 378"][MRFMESANO] += ESPVALORMOVRO
        if TPMOID == 8 and CMPID == 1028:
            self.df["Cruzamento 3 - 378"][MRFMESANO] += ESPVALORMOVRD
        # Cruzamento 4
        if TPMOID == 7 and CMPID == 1029:
            self.df["Cruzamento 4 - 378"][MRFMESANO] += ESPVALORMOVRO
        if TPMOID == 8 and CMPID == 1029:
            self.df["Cruzamento 4 - 378"][MRFMESANO] += ESPVALORMOVRD
        # Cruzamento 5
        if TPMOID == 9 and CMPID == 1030:
            self.df["Cruzamento 5 - 378"][MRFMESANO] += (
                ESPVALORMOVRD - ESPVALORCIRD)
        # Cruzamento 6
        if TPMOID == 9 and CMPID == 1031:
            self.df["Cruzamento 6 - 378"][MRFMESANO] += ESPVALORMOVRD
        # Cruzamento 7
        if TPMOID == 9 and CMPID == 1032:
            self.df["Cruzamento 7 - 378"][MRFMESANO] += ESPVALORMOVRD
        # Cruzamento 8
        if TPMOID == 9 and CMPID == 1033:
            self.df["Cruzamento 8 - 378"][MRFMESANO] += ESPVALORMOVRD
        # Cruzamento 9
        if TPMOID == 10 and CMPID == 1034:
            self.df["Cruzamento 9 - 378"][MRFMESANO] += ESPVALORMOVRD - ESPVALORCIRD
        # Cruzamento 10
        if TPMOID == 10 and CMPID == 1035:
            self.df["Cruzamento 10 - 378"][MRFMESANO] += ESPVALORMOVRD
        # Cruzamento 11
        if TPMOID == 10 and CMPID == 1036:
            self.df["Cruzamento 11 - 378"][MRFMESANO] += ESPVALORMOVRD
        # Cruzamento 12
        if TPMOID == 10 and CMPID == 1037:
            self.df["Cruzamento 12 - 378"][MRFMESANO] += ESPVALORMOVRD
        # Cruzamento 13
        if TPMOID == 7 and CMPID == 1026:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += ESPVALORCIRO
        if TPMOID == 8 and CMPID == 1026:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += ESPVALORCIRD
        if TPMOID == 9 and CMPID == 1026:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= ESPVALORCIRD
        if TPMOID == 10 and CMPID == 1026:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= ESPVALORCIRD
        if TPMOID == 7 and CMPID == 1030:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += ESPVALORCIRO
        if TPMOID == 8 and CMPID == 1030:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += ESPVALORCIRD
        if TPMOID == 9 and CMPID == 1030:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= ESPVALORCIRD
        if TPMOID == 10 and CMPID == 1030:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= ESPVALORCIRD
        if TPMOID == 7 and CMPID == 1034:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += ESPVALORCIRO
        if TPMOID == 8 and CMPID == 1034:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += ESPVALORCIRD
        if TPMOID == 9 and CMPID == 1034:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= ESPVALORCIRD
        if TPMOID == 10 and CMPID == 1034:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= ESPVALORCIRD
        # Cruzamento 14
        if TPMOID == 7 and CMPID == 1026:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += ESPVALORCARO
        if TPMOID == 8 and CMPID == 1026:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += ESPVALORCARD
        if TPMOID == 9 and CMPID == 1026:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 10 and CMPID == 1026:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 7 and CMPID == 1030:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += ESPVALORCARO
        if TPMOID == 8 and CMPID == 1030:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += ESPVALORCARD
        if TPMOID == 9 and CMPID == 1030:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 10 and CMPID == 1030:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 7 and CMPID == 1034:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += ESPVALORCARO
        if TPMOID == 8 and CMPID == 1034:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += ESPVALORCARD
        if TPMOID == 9 and CMPID == 1034:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 10 and CMPID == 1034:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= ESPVALORCARD
        # Cruzamento 15
        if TPMOID == 7 and CMPID == 1027:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += ESPVALORCARO
        if TPMOID == 8 and CMPID == 1027:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += ESPVALORCARD
        if TPMOID == 9 and CMPID == 1027:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 10 and CMPID == 1027:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 7 and CMPID == 1031:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += ESPVALORCARO
        if TPMOID == 8 and CMPID == 1031:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += ESPVALORCARD
        if TPMOID == 9 and CMPID == 1031:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 10 and CMPID == 1031:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 7 and CMPID == 1035:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += ESPVALORCARO
        if TPMOID == 8 and CMPID == 1035:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += ESPVALORCARD
        if TPMOID == 9 and CMPID == 1035:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 10 and CMPID == 1035:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= ESPVALORCARD
        # Cruzamento 16
        if TPMOID == 7 and CMPID == 1028:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += ESPVALORCARO
        if TPMOID == 8 and CMPID == 1028:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += ESPVALORCARD
        if TPMOID == 9 and CMPID == 1028:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 10 and CMPID == 1028:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 7 and CMPID == 1032:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += ESPVALORCARO
        if TPMOID == 8 and CMPID == 1032:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += ESPVALORCARD
        if TPMOID == 9 and CMPID == 1032:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 10 and CMPID == 1032:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 7 and CMPID == 1036:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += ESPVALORCARO
        if TPMOID == 8 and CMPID == 1036:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += ESPVALORCARD
        if TPMOID == 9 and CMPID == 1036:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= ESPVALORCARD
        if TPMOID == 10 and CMPID == 1036:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= ESPVALORCARD
