import pandas as pd
import calendar
from datetime import datetime


# RESEGUROS
class maths_409():

    def __init__(self, dates):
        self.df = pd.DataFrame(index=dates, columns=[
            f"Cruzamento {i} - 409" for i in range(1, 10)])
        self.df.fillna(0.0, inplace=True)

    def run(self, linha):
        MRFMESANO = linha[12:18]
        TPMORESSID = linha[18:21]
        MPRTIPOCONT = linha[60:61]
        MPRMODCONT = linha[61:63]
        MPRVALORMOV = linha[101:114]
        MPRVALORMOVCOMIS = linha[114:127]
        # Cruzamento 1
        # MPRTIPOCONT 1 ; MPRMODCONT 1+2 ; TPMORESSID 35+36-37-38+39 ;
        # MPRVALORMOV ; CMPID 12087
        if MPRTIPOCONT == "1" and MPRMODCONT in ["01","02"]:
            if TPMORESSID in ["035","036","038"]:
                self.df["Cruzamento 1 - 409"][MRFMESANO] += float(MPRVALORMOV)
            elif TPMORESSID in ["037","038"]:
                self.df["Cruzamento 1 - 409"][MRFMESANO] -= float(MPRVALORMOV)
        # Cruzamento 2
        # MPRTIPOCONT 1 ; MPRMODCONT 1+2 ; TPMORESSID 35+36-37-38+39 ;
        # MPRVALORMOVCOMISS ; CMPID 12089
        if MPRTIPOCONT == "1" and MPRMODCONT in ["01","02"]:
            if TPMORESSID in ["035","036","038"]:
                self.df["Cruzamento 2 - 409"][MRFMESANO] += float(MPRVALORMOVCOMIS)
            elif TPMORESSID in ["037","038"]:
                self.df["Cruzamento 2 - 409"][MRFMESANO] -= float(MPRVALORMOVCOMIS)
        # Cruzamento 3
        # MPRTIPOCONT 1 ; MPRMODCONT 1+2 ; TPMORESSID 40+41-42+43 ; MPRVALORMOV
        # ; CMPID 12090
        if MPRTIPOCONT == "1" and MPRMODCONT in ["01","02"]:
            if TPMORESSID in ["040","041","043"]:
                self.df["Cruzamento 3 - 409"][MRFMESANO] += float(MPRVALORMOV)
            elif TPMORESSID == "42":
                self.df["Cruzamento 3 - 409"][MRFMESANO] -= float(MPRVALORMOV)
        # Cruzamento 4
        # MPRTIPOCONT 1 ; MPRMODCONT 1+2 ; TPMORESSID 40+41-42+43 ;
        # MPRVALORMOVCOMISS ; CMPID 12092
        if MPRTIPOCONT == "1" and MPRMODCONT in ["01","02"]:
            if TPMORESSID in ["040","041","043"]:
                self.df["Cruzamento 4 - 409"][MRFMESANO] += float(MPRVALORMOVCOMIS)
            elif TPMORESSID == "042":
                self.df["Cruzamento 4 - 409"][MRFMESANO] -= float(MPRVALORMOVCOMIS)
        # Cruzamento 5
        # MPRTIPOCONT 1 ; MPRMODCONT 3+4+5+6 ; TPMORESSID 35+36-37-38 ;
        # MPRVALORMOV ; CMPID 12097
        if MPRTIPOCONT == "1" and MPRMODCONT in ["03","04","05","06"]:
            if TPMORESSID in ["035","036"]:
                self.df["Cruzamento 5 - 409"][MRFMESANO] += float(MPRVALORMOV)
            elif TPMORESSID in ["037","038"]:
                self.df["Cruzamento 5 - 409"][MRFMESANO] -= float(MPRVALORMOV)
        # Cruzamento 6
        # MPRTIPOCONT 1 ; MPRMODCONT 3+4+5+6 ; TPMORESSID 39 ; MPRVALORMOV ;
        # CMPID 12098
        if MPRTIPOCONT == "1" and MPRMODCONT in ["03","04","05","06"]:
            if TPMORESSID == "039":
                self.df["Cruzamento 6 - 409"][MRFMESANO] += float(MPRVALORMOV)
        # Cruzamento 7
        # MPRTIPOCONT 1 ; MPRMODCONT 3+4+5+6 ; TPMORESSID 44 ; MPRVALORMOV ;
        # CMPID 12099
        if MPRTIPOCONT == "1" and MPRMODCONT in ["03","04","05","06"]:
            if TPMORESSID == "044":
                self.df["Cruzamento 7 - 409"][MRFMESANO] += float(MPRVALORMOV)
        # Cruzamento 8
        # MPRTIPOCONT 2 ; MPRMODCONT 99 ; TPMORESSID 35+36-37-38 ; MPRVALORMOV
        # ; CMPID 12082-12085
        if MPRTIPOCONT == "2" and MPRMODCONT == "99":
            if TPMORESSID in ["035","036"]:
                self.df["Cruzamento 8 - 409"][MRFMESANO] += float(MPRVALORMOV)
            elif TPMORESSID in ["037","038"]:
                self.df["Cruzamento 8 - 409"][MRFMESANO] -= float(MPRVALORMOV)
        # Cruzamento 9
        # MPRTIPOCONT 2 ; MPRMODCONT 99 ; TPMORESSID 35+36-37-38 ;
        # MPRVALORMOVCOMISS ; CMPID 12084
        if MPRTIPOCONT == "2" and MPRMODCONT == "99":
            if TPMORESSID in ["035","036"]:
                self.df["Cruzamento 8 - 409"][MRFMESANO] += float(MPRVALORMOVCOMIS)
            elif TPMORESSID in ["037","038"]:
                self.df["Cruzamento 8 - 409"][MRFMESANO] -= float(MPRVALORMOVCOMIS)