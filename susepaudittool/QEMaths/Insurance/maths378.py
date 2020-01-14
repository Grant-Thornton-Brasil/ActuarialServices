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
        MRFMESANO= linha[12:20]                                                                                          
        TPMOID= linha[23:27]
        CMPID= linha[27:31]                                                                                                    
        ESPVALORMOVRO= linha[59:72]                                                                                         
        ESPDATAINICIORD= linha[72:80]                                                                                                                
        ESPVALORMOVRD= linha[96:109]                                                                                                                                                      
        ESPVALORCARO= linha[118:131] 
        ESPVALORCARD = linha[131:144]
        ESPVALORCIRO= linha[144:157]                                                                    
        ESPVALORCIRD= linha[157:170]                                                                                                        
        # Cruzamento 1
        if int(TPMOID) in [7,8] and int(CMPID) == 1026:
            self.df["Cruzamento 1 - 378"][MRFMESANO] += (float(ESPVALORMOVRO) - float(ESPVALORCIRO))
        # Cruzamento 2
        if int(TPMOID) in [7,8] and int(CMPID) == 1027:
            self.df["Cruzamento 2 - 378"][MRFMESANO] += float(ESPVALORMOVRO)
        # Cruzamento 3
        if int(TPMOID) in [7,8] and int(CMPID) == 1028:
            self.df["Cruzamento 3 - 378"][MRFMESANO] += float(ESPVALORMOVRO)
        # Cruzamento 4
        if int(TPMOID) in [7,8] and int(CMPID) == 1029:
            self.df["Cruzamento 4 - 378"][MRFMESANO] += float(ESPVALORMOVRO)
        # Cruzamento 5
        if int(TPMOID) == 9 and int(CMPID) == 1030:
            self.df["Cruzamento 5 - 378"][MRFMESANO] += (float(ESPVALORMOVRD) - float(ESPVALORCIRO))
        # Cruzamento 6
        if int(TPMOID) == 9 and int(CMPID) == 1031:
            self.df["Cruzamento 6 - 378"][MRFMESANO] += float(ESPVALORMOVRD)
        # Cruzamento 7
        if int(TPMOID) == 9 and int(CMPID) == 1032:
            self.df["Cruzamento 7 - 378"][MRFMESANO] += float(ESPVALORMOVRD)
        # Cruzamento 8
        if int(TPMOID) == 9 and int(CMPID) == 1033:
            self.df["Cruzamento 8 - 378"][MRFMESANO] += float(ESPVALORMOVRD)
        # Cruzamento 9
        if int(TPMOID) == 10 and int(CMPID) == 1034:
            self.df["Cruzamento 9 - 378"][MRFMESANO] += (float(ESPVALORMOVRD) - float(ESPVALORCIRD))
        # Cruzamento 10
        if int(TPMOID) == 10 and int(CMPID) == 1035:
            self.df["Cruzamento 10 - 378"][MRFMESANO] += float(ESPVALORMOVRD)
        # Cruzamento 11
        if int(TPMOID) == 10 and int(CMPID) == 1036:
            self.df["Cruzamento 11 - 378"][MRFMESANO] += float(ESPVALORMOVRD)
        # Cruzamento 12
        if int(TPMOID) == 10 and int(CMPID) == 1037:
            self.df["Cruzamento 12 - 378"][MRFMESANO] += float(ESPVALORMOVRD)
        # Cruzamento 13
        if int(TPMOID) == 7 and int(CMPID) == 1026:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += float(ESPVALORCIRO)
        if int(TPMOID) == 8 and int(CMPID) == 1026:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += float(ESPVALORCIRD)
        if int(TPMOID) == 9 and int(CMPID) == 1026:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= float(ESPVALORCIRD)
        if int(TPMOID) == 10 and int(CMPID) == 1026:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= float(ESPVALORCIRD)
        if int(TPMOID) == 7 and int(CMPID) == 1030:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += float(ESPVALORCIRO)
        if int(TPMOID) == 8 and int(CMPID) == 1030:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += float(ESPVALORCIRD)
        if int(TPMOID) == 9 and int(CMPID) == 1030:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= float(ESPVALORCIRD)
        if int(TPMOID) == 10 and int(CMPID) == 1030:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= float(ESPVALORCIRD)
        if int(TPMOID) == 7 and int(CMPID) == 1034:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += float(ESPVALORCIRO)
        if int(TPMOID) == 8 and int(CMPID) == 1034:
            self.df["Cruzamento 13 - 378"][MRFMESANO] += float(ESPVALORCIRD)
        if int(TPMOID) == 9 and int(CMPID) == 1034:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= float(ESPVALORCIRD)
        if int(TPMOID) == 10 and int(CMPID) == 1034:
            self.df["Cruzamento 13 - 378"][MRFMESANO] -= float(ESPVALORCIRD)
        # Cruzamento 14
        if int(TPMOID) == 7 and int(CMPID) == 1026:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += float(ESPVALORCARO)
        if int(TPMOID) == 8 and int(CMPID) == 1026:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += float(ESPVALORCARD)
        if int(TPMOID) == 9 and int(CMPID) == 1026:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 10 and int(CMPID) == 1026:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 7 and int(CMPID) == 1030:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += float(ESPVALORCARO)
        if int(TPMOID) == 8 and int(CMPID) == 1030:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += float(ESPVALORCARD)
        if int(TPMOID) == 9 and int(CMPID) == 1030:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 10 and int(CMPID) == 1030:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 7 and int(CMPID) == 1034:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += float(ESPVALORCARO)
        if int(TPMOID) == 8 and int(CMPID) == 1034:
            self.df["Cruzamento 14 - 378"][MRFMESANO] += float(ESPVALORCARD)
        if int(TPMOID) == 9 and int(CMPID) == 1034:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 10 and int(CMPID) == 1034:
            self.df["Cruzamento 14 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        # Cruzamento 15
        if int(TPMOID) == 7 and int(CMPID) == 1027:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += float(ESPVALORCARO)
        if int(TPMOID) == 8 and int(CMPID) == 1027:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += float(ESPVALORCARD)
        if int(TPMOID) == 9 and int(CMPID) == 1027:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 10 and int(CMPID) == 1027:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 7 and int(CMPID) == 1031:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += float(ESPVALORCARO)
        if int(TPMOID) == 8 and int(CMPID) == 1031:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += float(ESPVALORCARD)
        if int(TPMOID) == 9 and int(CMPID) == 1031:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 10 and int(CMPID) == 1031:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 7 and int(CMPID) == 1035:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += float(ESPVALORCARO)
        if int(TPMOID) == 8 and int(CMPID) == 1035:
            self.df["Cruzamento 15 - 378"][MRFMESANO] += float(ESPVALORCARD)
        if int(TPMOID) == 9 and int(CMPID) == 1035:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 10 and int(CMPID) == 1035:
            self.df["Cruzamento 15 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        # Cruzamento 16
        if int(TPMOID) == 7 and int(CMPID) == 1028:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += float(ESPVALORCARO)
        if int(TPMOID) == 8 and int(CMPID) == 1028:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += float(ESPVALORCARD)
        if int(TPMOID) == 9 and int(CMPID) == 1028:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 10 and int(CMPID) == 1028:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 7 and int(CMPID) == 1032:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += float(ESPVALORCARO)
        if int(TPMOID) == 8 and int(CMPID) == 1032:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += float(ESPVALORCARD)
        if int(TPMOID) == 9 and int(CMPID) == 1032:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 10 and int(CMPID) == 1032:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 7 and int(CMPID) == 1036:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += float(ESPVALORCARO)
        if int(TPMOID) == 8 and int(CMPID) == 1036:
            self.df["Cruzamento 16 - 378"][MRFMESANO] += float(ESPVALORCARD)
        if int(TPMOID) == 9 and int(CMPID) == 1036:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= float(ESPVALORCARD)
        if int(TPMOID) == 10 and int(CMPID) == 1036:
            self.df["Cruzamento 16 - 378"][MRFMESANO] -= float(ESPVALORCARD)