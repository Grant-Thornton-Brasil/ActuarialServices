import pandas as pd
import calendar
from datetime import datetime


# RESEGUROS
class maths_405():

    def __init__(self, dates):
        self.df = pd.DataFrame(index=dates, columns=[
            f"Cruzamento {i} - 405" for i in range(1, 6)])
        self.df.fillna(0.0, inplace=True)

    def run(self, linha):
        MRFMESANO = linha[12:18]
        TPMORESSID = linha[18:21]
        MSRVALORMOV = linha[99:112]
        MSRTIPOSIN = linha[112:113]
        # Cruzamento 1
        # TPMORESSID 12+14-19+21 ; MSRTIPOSIN 1 ; MSRVALORMOV ; CMPID 12258
        if MSRTIPOSIN == "1":
            if TPMORESSID in ["012", "014", "021"]:
                self.df["Cruzamento 1 - 405"][MRFMESANO] += float(MSRVALORMOV)
            elif TPMORESSID == "019":
                self.df["Cruzamento 1 - 405"][MRFMESANO] -= float(MSRVALORMOV) 
        # Cruzamento 2
        # TPMORESSID 12+14-19+21 ; MSRTIPOSIN 2 ; MSRVALORMOV ; CMPID 12259
        if MSRTIPOSIN == "2":
            if TPMORESSID in ["012", "014", "021"]:
                self.df["Cruzamento 2 - 405"][MRFMESANO] += float(MSRVALORMOV) 
            elif TPMORESSID == "019":
                self.df["Cruzamento 2 - 405"][MRFMESANO] -= float(MSRVALORMOV) 
        # Cruzamento 3
        # TPMORESSID 13+15-20+22 ; MSRTIPOSIN 1 ; MSRVALORMOV ; CMPID 12262
        if MSRTIPOSIN == "1":
            if TPMORESSID in ["013", "015", "022"]:
                self.df["Cruzamento 3 - 405"][MRFMESANO] += float(MSRVALORMOV) 
            elif TPMORESSID == "020":
                self.df["Cruzamento 3 - 405"][MRFMESANO] -= float(MSRVALORMOV) 
        # Cruzamento 4
        # TPMORESSID 13+15-20+22 ; MSRTIPOSIN 2 ; MSRVALORMOV ; CMPID 12263
        if MSRTIPOSIN == "2":
            if TPMORESSID in ["013", "015", "022"]:
                self.df["Cruzamento 4 - 405"][MRFMESANO] += float(MSRVALORMOV) 
            elif TPMORESSID == "020":
                self.df["Cruzamento 4 - 405"][MRFMESANO] -= float(MSRVALORMOV) 
        # Cruzamento 5
        # TPMORESSID 14-19+21 ; MSRTIPOSIN 1+2 ; MSRVALORMOV ; CMPID 12273
        if MSRTIPOSIN in ["1", "2"]:
            if TPMORESSID in ["014", "021"]:
                self.df["Cruzamento 5 - 405"][MRFMESANO] += float(MSRVALORMOV) 
            elif TPMORESSID == "019":
                self.df["Cruzamento 5 - 405"][MRFMESANO] -= float(MSRVALORMOV) 