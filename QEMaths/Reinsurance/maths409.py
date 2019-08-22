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
        # Cruzamento 1
        # MPRTIPOCONT 1 ; MPRMODCONT 1+2 ; TPMORESSID 35+36-37-38+39 ;
        # MPRVALORMOV ; CMPID 12087
        if linha[60] == "1" and linha[62] in [
                "01", "02"] and linha[18:21] in ["035", "036", "39"]:
            self.df["Cruzamento 1 - 409"][linha[12:18]] \
                += float(linha[101:114])
        if linha[60] == "1" and linha[62] in [
                "01", "02"] and linha[18:21] in ["037", "038"]:
            self.df["Cruzamento 1 - 409"][linha[12:18]] \
                -= float(linha[101:114])
        # Cruzamento 2
        # MPRTIPOCONT 1 ; MPRMODCONT 1+2 ; TPMORESSID 35+36-37-38+39 ;
        # MPRVALORMOVCOMISS ; CMPID 12089
        if linha[60] == "1" and linha[62] in [
                "01", "02"] and linha[18:21] in ["035", "036", "39"]:
            self.df["Cruzamento 1 - 409"][linha[12:18]] \
                += float(linha[114:127])
        if linha[60] == "1" and linha[62] in [
                "01", "02"] and linha[18:21] in ["037", "038"]:
            self.df["Cruzamento 1 - 409"][linha[12:18]] \
                -= float(linha[114:127])
        # Cruzamento 3
        # MPRTIPOCONT 1 ; MPRMODCONT 1+2 ; TPMORESSID 40+41-42+43 ; MPRVALORMOV
        # ; CMPID 12090
        if linha[60] == "1" and linha[62] in [
                "01", "02"] and linha[18:21] in ["040", "041", "043"]:
            self.df["Cruzamento 3 - 409"][linha[12:18]] \
                += float(linha[101:114])
        if linha[60] == "1" and linha[62] in [
                "01", "02"] and linha[18:21] == "042":
            self.df["Cruzamento 3 - 409"][linha[12:18]] \
                -= float(linha[101:114])
        # Cruzamento 4
        # MPRTIPOCONT 1 ; MPRMODCONT 1+2 ; TPMORESSID 40+41-42+43 ;
        # MPRVALORMOVCOMISS ; CMPID 12092
        if linha[60] == "1" and linha[62] in [
                "01", "02"] and linha[18:21] in ["040", "041", "043"]:
            self.df["Cruzamento 4 - 409"][linha[12:18]] \
                += float(linha[114:127])
        if linha[60] == "1" and linha[62] in [
                "01", "02"] and linha[18:21] == "042":
            self.df["Cruzamento 4 - 409"][linha[12:18]] \
                -= float(linha[114:127])
        # Cruzamento 5
        # MPRTIPOCONT 1 ; MPRMODCONT 3+4+5+6 ; TPMORESSID 35+36-37-38 ;
        # MPRVALORMOV ; CMPID 12097
        if linha[60] == "1" and linha[62] in ["03", "04",
                                              "05", "06"] and linha[18:21] in ["035", "036"]:
            self.df["Cruzamento 5 - 409"][linha[12:18]] \
                += float(linha[101:114])
        if linha[60] == "1" and linha[62] in ["03", "04",
                                              "05", "06"] and linha[18:21] in ["037", "038"]:
            self.df["Cruzamento 5 - 409"][linha[12:18]] \
                += float(linha[101:114])
        # Cruzamento 6
        # MPRTIPOCONT 1 ; MPRMODCONT 3+4+5+6 ; TPMORESSID 39 ; MPRVALORMOV ;
        # CMPID 12098
        if linha[60] == "1" and linha[62] in [
                "03", "04", "05", "06"] and linha[18:21] == "039":
            self.df["Cruzamento 6 - 409"][linha[12:18]] \
                += float(linha[101:114])
        # Cruzamento 7
        # MPRTIPOCONT 1 ; MPRMODCONT 3+4+5+6 ; TPMORESSID 44 ; MPRVALORMOV ;
        # CMPID 12099
        if linha[60] == "1" and linha[62] in [
                "03", "04", "05", "06"] and linha[18:21] == "044":
            self.df["Cruzamento 7 - 409"][linha[12:18]] \
                += float(linha[101:114])
        # Cruzamento 8
        # MPRTIPOCONT 2 ; MPRMODCONT 99 ; TPMORESSID 35+36-37-38 ; MPRVALORMOV
        # ; CMPID 12082-12085
        if linha[60] == "2" and linha[62] == "99" and linha[18:21] in [
                "035", "036"]:
            self.df["Cruzamento 8 - 409"][linha[12:18]] \
                += float(linha[101:114])
        if linha[60] == "2" and linha[62] == "99" and linha[18:21] in [
                "037", "038"]:
            self.df["Cruzamento 8 - 409"][linha[12:18]] \
                -= float(linha[101:114])
        # Cruzamento 9
        # MPRTIPOCONT 2 ; MPRMODCONT 99 ; TPMORESSID 35+36-37-38 ;
        # MPRVALORMOVCOMISS ; CMPID 12084
        if linha[60] == "2" and linha[62] == "99" and linha[18:21] in [
                "035", "036"]:
            self.df["Cruzamento 9 - 409"][linha[12:18]] \
                += float(linha[114:127])
        if linha[60] == "2" and linha[62] == "99" and linha[18:21] in [
                "037", "038"]:
            self.df["Cruzamento 9 - 409"][linha[12:18]] \
                -= float(linha[114:127])