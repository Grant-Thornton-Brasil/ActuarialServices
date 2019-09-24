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
        # Cruzamento 1
        # MPATIPOCONT 1 ; MPAMODCONT 1+2 ; MPATIPOPERA 1 ; TPMORESSID
        # 24+25-26-27+28 ; MPAVALORMOV ; CMPID 12064
        if linha[61] == "1" and linha[62] in [
                "01", "02"] and linha[23] == "1" and linha[18:21] in ["024", "025", "028"]:
            self.df["Cruzamento 1 - 408"][linha[12:18]] \
                += float(linha[96:109])
        if linha[61] == "1" and linha[62] in [
                "01", "02"] and linha[23] == "1" and linha[18:21] in ["026", "027"]:
            self.df["Cruzamento 1 - 408"][linha[12:18]] \
                -= float(linha[96:109])
        # Cruzamento 2
        # MPATIPOCONT 1 ; MPAMODCONT 1+2 ; MPATIPOPERA 1 ; TPMORESSID
        # 24+25-26-27+28 ; MPAVALORMOVCOMISS ; CMPID 12066
        if linha[61] == "1" and linha[62] in [
                "01", "02"] and linha[23] == "1" and linha[18:21] in ["024", "025", "028"]:
            self.df["Cruzamento 2 - 408"][linha[12:18]] \
                += float(linha[115:128])
        if linha[61] == "1" and linha[62] in [
                "01", "02"] and linha[23] == "1" and linha[18:21] in ["026", "027"]:
            self.df["Cruzamento 2 - 408"][linha[12:18]] \
                -= float(linha[115:128])
        # Cruzamento 3
        # MPATIPOCONT 1 ; MPAMODCONT 1+2 ; MPATIPOPERA 1 ; TPMORESSID
        # 29+30-31+32 ; MPAVALORMOV ; CMPID 12067
        if linha[61] == "1" and linha[62] in [
                "01", "02"] and linha[23] == "1" and linha[18:21] in ["029", "030", "032"]:
            self.df["Cruzamento 3 - 408"][linha[12:18]] \
                += float(linha[96:109])
        if linha[61] == "1" and linha[62] in ["01",
                                              "02"] and linha[23] == "1" and linha[18:21] == "031":
            self.df["Cruzamento 3 - 408"][linha[12:18]] \
                -= float(linha[96:109])
        # Cruzamento 4
        # MPATIPOCONT 1 ; MPAMODCONT 1+2 ; MPATIPOPERA 1 ; TPMORESSID
        # 29+30-31+32 ; MPAVALORMOVCOMISS ; CMPID 12069
        if linha[61] == "1" and linha[62] in [
                "01", "02"] and linha[23] == "1" and linha[18:21] in ["029", "030", "032"]:
            self.df["Cruzamento 3 - 408"][linha[12:18]] \
                += float(linha[115:128])
        if linha[61] == "1" and linha[62] in ["01",
                                              "02"] and linha[23] == "1" and linha[18:21] == "031":
            self.df["Cruzamento 3 - 408"][linha[12:18]] \
                -= float(linha[115:128])
        # Cruzamento 5
        # MPATIPOCONT 1 ; MPAMODCONT 3+4+5+6 ; MPATIPOPERA 1 ; TPMORESSID
        # 24+25-16-27 ; MPAVALORMOV ; CMPID 12074
        if linha[61] == "1" and linha[62] in ["03", "04", "05",
                                              "06"] and linha[23] == "1" and linha[18:21] in ["024", "025"]:
            self.df["Cruzamento 5 - 408"][linha[12:18]] \
                += float(linha[96:109])
        if linha[61] == "1" and linha[62] in ["03", "04", "05",
                                              "06"] and linha[23] == "1" and linha[18:21] in ["016", "027"]:
            self.df["Cruzamento 5 - 408"][linha[12:18]] \
                -= float(linha[96:109])
        # Cruzamento 6
        # MPATIPOCONT 1 ; MPAMODCONT 3+4+5+6 ; MPATIPOPERA 1 ; TPMORESSID 28 ;
        # MPAVALORMOV ; CMPID 12075
        if linha[61] == "1" and linha[62] in ["03", "04", "05",
                                              "06"] and linha[23] == "1" and linha[18:21] == "028":
            self.df["Cruzamento 6 - 408"][linha[12:18]] \
                += float(linha[96:109])
        # Cruzamento 7
        # MPATIPOCONT 1 ; MPAMODCONT 3+4+5+6 ; MPATIPOPERA 1 ; TPMORESSID 33 ;
        # MPAVALORMOV ; CMPID 12076
        if linha[61] == "1" and linha[62] in ["03", "04", "05",
                                              "06"] and linha[23] == "1" and linha[18:21] == "033":
            self.df["Cruzamento 7 - 408"][linha[12:18]] \
                += float(linha[96:109])
        # Cruzamento 8
        # MPATIPOCONT 2 ; MPAMODCONT 99 ; MPATIPOPERA 1 ; TPMORESSID
        # 24+25-26-27 ; MPAVALORMOV ; CMPID 12059-12062
        if linha[61] == "2" and linha[62] == "99" and linha[23] == "1" and linha[18:21] == [
                "024", "025"]:
            self.df["Cruzamento 8 - 408"][linha[12:18]] \
                += float(linha[96:109])
        if linha[61] == "2" and linha[62] == "99" and linha[23] == "1" and linha[18:21] == [
                "026", "027"]:
            self.df["Cruzamento 8 - 408"][linha[12:18]] \
                -= float(linha[96:109])
        # Cruzamento 9
        # MPATIPOCONT 2 ; MPAMODCONT 99 ; MPATIPOPERA 1 ; TPMORESSID
        # 24+25-26-27 ; MPAVALORMOVCOMISS ; CMPID 12061
        if linha[61] == "2" and linha[62] == "99" and linha[23] == "1" and linha[18:21] == [
                "024", "025"]:
            self.df["Cruzamento 8 - 408"][linha[12:18]] \
                += float(linha[115:128])
        if linha[61] == "2" and linha[62] == "99" and linha[23] == "1" and linha[18:21] == [
                "026", "027"]:
            self.df["Cruzamento 8 - 408"][linha[12:18]] \
                -= float(linha[115:128])
        # Cruzamento 10
        # MPATIPOCONT 1+2 ; MPAMODCONT 1+2+3+4+5+6+99 ; MPATIPOPERA 2 ;
        # TPMORESSID 24+25-26-27+28+29+30-31+32+33 ; MPAVALORMOVCOMISS ; CMPID
        # 12078
        if linha[18:21] in ["24", "25", "28", "29", "30", "32", "33"]:
            self.df["Cruzamento 10 - 408"][linha[12:18]] \
                += float(linha[96:109])
        if linha[18:21] in ["26", "27", "31"]:
            self.df["Cruzamento 10 - 408"][linha[12:18]] \
                -= float(linha[96:109])
        # Cruzamento 11
        # TPMORESSID 24+25-26-27+28+29+30-31+32 MPAVALORMOVCORRET CMPID 12500
        if linha[18:21] in ["24", "25", "28", "29", "30", "32"]:
            self.df["Cruzamento 11 - 408"][linha[12:18]] \
                += float(linha[115:128])
        if linha[18:21] in ["26", "27", "31"]:
            self.df["Cruzamento 11 - 408"][linha[12:18]] \
                -= float(linha[115:128])