import pandas as pd
import calendar
from datetime import datetime


# RESEGUROS
class maths_408():

    def __init__(self, dates):
        self.df = pd.DataFrame(index=dates, columns=[
            f"Cruzamento {i} - 408" for i in range(1, 12)])
        self.df.fillna(0.0, inplace=True)

    def run(self, linha):
        MRFMESANO = linha[12:18]
        TPMORESSID = linha[18:21]
        MPATIPOPERA = linha[23:24]
        MPATIPOCONT = linha[61:62]
        MPAMODCONT = linha[62:64]
        MPAVALORMOV = linha[96:109]
        MPAVALORMOVCORRET = linha[128:141]
        MPAVALORMOVCOMIS = linha[115:128]
        # Cruzamento 1
        # MPATIPOCONT 1 ; MPAMODCONT 1+2 ; MPATIPOPERA 1 ; TPMORESSID
        # 24+25-26-27+28 ; MPAVALORMOV ; CMPID 12064
        if MPATIPOCONT == "1" and MPAMODCONT in ["01","02"] and MPATIPOPERA == "1":
            if TPMORESSID in ["024","025","028"]:
                self.df["Cruzamento 1 - 408"][MRFMESANO] += float(MPAVALORMOV)
            elif TPMORESSID in ["026","027"]:
                self.df["Cruzamento 1 - 408"][MRFMESANO] -= float(MPAVALORMOV)
        # Cruzamento 2
        # MPATIPOCONT 1 ; MPAMODCONT 1+2 ; MPATIPOPERA 1 ; TPMORESSID
        # 24+25-26-27+28 ; MPAVALORMOVCOMISS ; CMPID 12066
        if MPATIPOCONT == "1" and MPAMODCONT in ["01","02"] and MPATIPOPERA == "1":
            if TPMORESSID in ["024","025","028"]:
                self.df["Cruzamento 2 - 408"][MRFMESANO] += float(MPAVALORMOVCOMIS)
            elif TPMORESSID in ["026","027"]:
                self.df["Cruzamento 2 - 408"][MRFMESANO] -= float(MPAVALORMOVCOMIS)
        # Cruzamento 3
        # MPATIPOCONT 1 ; MPAMODCONT 1+2 ; MPATIPOPERA 1 ; TPMORESSID
        # 29+30-31+32 ; MPAVALORMOV ; CMPID 12067
        if MPATIPOCONT == "1" and MPAMODCONT in ["01","02"] and MPATIPOPERA == "1":
            if TPMORESSID in ["029","030","032"]:
                self.df["Cruzamento 3 - 408"][MRFMESANO] += float(MPAVALORMOV)
            elif TPMORESSID == "031":
                self.df["Cruzamento 3 - 408"][MRFMESANO] -= float(MPAVALORMOV)
        # Cruzamento 4
        # MPATIPOCONT 1 ; MPAMODCONT 1+2 ; MPATIPOPERA 1 ; TPMORESSID
        # 29+30-31+32 ; MPAVALORMOVCOMISS ; CMPID 12069
        if MPATIPOCONT == "1" and MPAMODCONT in ["01","02"] and MPATIPOPERA == "1":
            if TPMORESSID in ["029","030","032"]:
                self.df["Cruzamento 4 - 408"][MRFMESANO] += float(MPAVALORMOVCOMIS)
            elif TPMORESSID == "031":
                self.df["Cruzamento 4 - 408"][MRFMESANO] -= float(MPAVALORMOVCOMIS)
        # Cruzamento 5
        # MPATIPOCONT 1 ; MPAMODCONT 3+4+5+6 ; MPATIPOPERA 1 ; TPMORESSID
        # 24+25-26-27 ; MPAVALORMOV ; CMPID 12074
        if MPATIPOCONT == "1" and MPAMODCONT in ["03","04","05","06"] and MPATIPOPERA == "1":
            if TPMORESSID in ["024","025"]:
                self.df["Cruzamento 5 - 408"][MRFMESANO] += float(MPAVALORMOV)
            elif TPMORESSID in ["026","027"]:
                self.df["Cruzamento 5 - 408"][MRFMESANO] -= float(MPAVALORMOV)
        # Cruzamento 6
        # MPATIPOCONT 1 ; MPAMODCONT 3+4+5+6 ; MPATIPOPERA 1 ; TPMORESSID 28 ;
        # MPAVALORMOV ; CMPID 12075
        if MPATIPOCONT == "1" and MPAMODCONT in ["03","04","05","06"] and MPATIPOPERA == "1":
            if TPMORESSID == "028":
                self.df["Cruzamento 6 - 408"][MRFMESANO] += float(MPAVALORMOV)
        # Cruzamento 7
        # MPATIPOCONT 1 ; MPAMODCONT 3+4+5+6 ; MPATIPOPERA 1 ; TPMORESSID 33 ;
        # MPAVALORMOV ; CMPID 12076
        if MPATIPOCONT == "1" and MPAMODCONT in ["03","04","05","06"] and MPATIPOPERA == "1":
            if TPMORESSID == "033":
                self.df["Cruzamento 7 - 408"][MRFMESANO] += float(MPAVALORMOV)
        # Cruzamento 8
        # MPATIPOCONT 2 ; MPAMODCONT 99 ; MPATIPOPERA 1 ; TPMORESSID
        # 24+25-26-27 ; MPAVALORMOV ; CMPID 12059-12062
        if MPATIPOCONT == "2" and MPAMODCONT == "99" and MPATIPOPERA == "1":
            if TPMORESSID in ["024","025"]:
                self.df["Cruzamento 8 - 408"][MRFMESANO] += float(MPAVALORMOV)
            elif TPMORESSID in ["026","027"]:
                self.df["Cruzamento 8 - 408"][MRFMESANO] -= float(MPAVALORMOV)
        # Cruzamento 9
        # MPATIPOCONT 2 ; MPAMODCONT 99 ; MPATIPOPERA 1 ; TPMORESSID
        # 24+25-26-27 ; MPAVALORMOVCOMISS ; CMPID 12061
        if MPATIPOCONT == "2" and MPAMODCONT == "99" and MPATIPOPERA == "1":
            if TPMORESSID in ["024","025"]:
                self.df["Cruzamento 9 - 408"][MRFMESANO] += float(MPAVALORMOVCOMIS)
            elif TPMORESSID in ["026","027"]:
                self.df["Cruzamento 9 - 408"][MRFMESANO] -= float(MPAVALORMOVCOMIS)
        # Cruzamento 10
        # MPATIPOCONT 1+2 ; MPAMODCONT 1+2+3+4+5+6+99 ; MPATIPOPERA 2 ;
        # TPMORESSID 24+25-26-27+28+29+30-31+32+33 ; MPAVALORMOVCOMISS ; CMPID
        # 12078
        if MPATIPOCONT in ["1","2"] and MPAMODCONT in ["01","02","03","04","05","06","99"] and MPATIPOPERA == "2":
            if TPMORESSID in ["024","025","028","029","030","032","033"]:
                self.df["Cruzamento 10 - 408"][MRFMESANO] += float(MPAVALORMOVCOMIS)
            elif TPMORESSID in ["026","027","030"]:
                self.df["Cruzamento 10 - 408"][MRFMESANO] -= float(MPAVALORMOVCOMIS)
        # Cruzamento 11
        # TPMORESSID 24+25-26-27+28+29+30-31+32 MPAVALORMOVCORRET CMPID 12500
        if TPMORESSID in ["024", "025", "028", "029", "030", "032"]:
            self.df["Cruzamento 11 - 408"][MRFMESANO] += float(MPAVALORMOVCORRET)
        if TPMORESSID in ["026", "027", "031"]:
            self.df["Cruzamento 11 - 408"][MRFMESANO] -= float(MPAVALORMOVCORRET)