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
        # Cruzamento 1
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1026:
            self.df["Cruzamento 1 - 378"][linha[12:20]] \
                += (float(linha[59:72]) - float(linha[144:157]))
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1026:
            self.df["Cruzamento 1 - 378"][linha[12:20]] \
                += (float(linha[72:80]) - float(linha[157:170]))
        # Cruzamento 2
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1027:
            self.df["Cruzamento 2 - 378"][linha[12:20]] += float(linha[59:72])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1027:
            self.df["Cruzamento 2 - 378"][linha[12:20]] += float(linha[72:80])
        # Cruzamento 3
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1028:
            self.df["Cruzamento 3 - 378"][linha[12:20]] += float(linha[59:72])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1028:
            self.df["Cruzamento 3 - 378"][linha[12:20]] += float(linha[72:80])
        # Cruzamento 4
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1029:
            self.df["Cruzamento 4 - 378"][linha[12:20]] += float(linha[59:72])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1029:
            self.df["Cruzamento 4 - 378"][linha[12:20]] += float(linha[72:80])
        # Cruzamento 5
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1030:
            self.df["Cruzamento 5 - 378"][linha[12:20]] \
                += (float(linha[96:109]) - float(linha[144:157]))
        # Cruzamento 6
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1031:
            self.df["Cruzamento 6 - 378"][linha[12:20]] += float(linha[96:109])
        # Cruzamento 7
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1032:
            self.df["Cruzamento 7 - 378"][linha[12:20]] += float(linha[96:109])
        # Cruzamento 8
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1033:
            self.df["Cruzamento 8 - 378"][linha[12:20]] += float(linha[96:109])
        # Cruzamento 9
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1034:
            self.df["Cruzamento 9 - 378"][linha[12:20]] \
                += (float(linha[96:109]) - float(linha[157:170]))
        # Cruzamento 10
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1035:
            self.df["Cruzamento 10 - 378"][linha[12:20]] \
                += float(linha[96:109])
        # Cruzamento 11
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1036:
            self.df["Cruzamento 11 - 378"][linha[12:20]] \
                += float(linha[96:109])
        # Cruzamento 12
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1037:
            self.df["Cruzamento 12 - 378"][linha[12:20]] \
                += float(linha[96:109])
        # Cruzamento 13
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1026:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] += float(linha[144:157])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1026:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] += float(linha[157:170])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1026:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] -= float(linha[157:170])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1026:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] -= float(linha[157:170])
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1030:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] += float(linha[144:157])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1030:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] += float(linha[157:170])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1030:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] -= float(linha[157:170])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1030:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] -= float(linha[157:170])
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1034:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] += float(linha[144:157])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1034:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] += float(linha[157:170])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1034:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] -= float(linha[157:170])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1034:
            self.df["Cruzamento 13 - 378"][linha[12:20]
                                           ] -= float(linha[157:170])
        # Cruzamento 14
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1026:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] += float(linha[118:131])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1026:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] += float(linha[131:144])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1026:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1026:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1030:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] += float(linha[118:131])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1030:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] += float(linha[131:144])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1030:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1030:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1034:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] += float(linha[118:131])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1034:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] += float(linha[131:144])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1034:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1034:
            self.df["Cruzamento 14 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        # Cruzamento 15
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1027:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] += float(linha[118:131])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1027:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] += float(linha[131:144])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1027:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1027:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1031:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] += float(linha[118:131])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1031:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] += float(linha[131:144])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1031:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1031:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1035:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] += float(linha[118:131])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1035:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] += float(linha[131:144])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1035:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1035:
            self.df["Cruzamento 15 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        # Cruzamento 16
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1028:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] += float(linha[118:131])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1028:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] += float(linha[131:144])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1028:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1028:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1032:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] += float(linha[118:131])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1032:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] += float(linha[131:144])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1032:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1032:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 7 and int(linha[27:31]) == 1036:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] += float(linha[118:131])
        if int(linha[23:27]) == 8 and int(linha[27:31]) == 1036:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] += float(linha[131:144])
        if int(linha[23:27]) == 9 and int(linha[27:31]) == 1036:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])
        if int(linha[23:27]) == 10 and int(linha[27:31]) == 1036:
            self.df["Cruzamento 16 - 378"][linha[12:20]
                                           ] -= float(linha[131:144])