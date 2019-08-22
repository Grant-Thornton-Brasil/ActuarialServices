def qe_export(qe_type):
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    arquivos = list(filedialog.askopenfilenames(
        filetypes=[("Arquivos TXT", "*.txt")]))
    if qe_type == "376":
        with open("Export 376.csv", "a+") as csv:
            headers = [
                "ESRSEQ",
                "ENTCODIGO",
                "MRFMESANO",
                "QUAID",
                "TPMOID",
                "CMPID",
                "RAMCODIGO",
                "ESRDATAINICIO",
                "ESRDATAFIM",
                "ESRDATAOCORR",
                "ESRDATAREG",
                "ESRVALORMOV",
                "ESRDATACOMUNICA",
                "ESRCODCESS",
                "ESRNUMSIN",
                "ESRVALORMON"]
            csv.write(";".join(headers) + "\n")
            for arquivo in arquivos:
                with open(arquivo) as txt:
                    for linha in txt.readlines():
                        linha = linha.strip()
                        structure = [
                            linha[0:7],
                            linha[7:12],
                            linha[12:20],
                            linha[20:23],
                            linha[23:27],
                            linha[27:31],
                            linha[31:35],
                            linha[35:43],
                            linha[43:51],
                            linha[51:59],
                            linha[59:67],
                            linha[67:80],
                            linha[80:88],
                            linha[88:93],
                            linha[93:113],
                            linha[113:126]]
                        csv.write(";".join(structure) + "\n")
    elif qe_type == "377":
        with open("Export 377.csv", "a+") as csv:
            headers = [
                "ESLSEQ",
                "ENTCODIGO",
                "MRFMESANO",
                "QUAID",
                "CMPID",
                "RAMCODIGO",
                "ESLDATAINICIO",
                "ESLDATAFIM",
                "ESLDATAOCORR",
                "ESLDATAREG",
                "ESLVALORMOV",
                "ESLCODCESS",
                "ESLNUMSIN"]
            csv.write(";".join(headers) + "\n")
            for arquivo in arquivos:
                with open(arquivo) as txt:
                    for linha in txt.readlines():
                        linha = linha.strip()
                        structure = [
                            linha[0:7],
                            linha[7:12],
                            linha[12:20],
                            linha[20:23],
                            linha[23:27],
                            linha[27:31],
                            linha[31:39],
                            linha[39:47],
                            linha[47:55],
                            linha[55:63],
                            linha[63:76],
                            linha[76:81],
                            linha[81:101]]
                        csv.write(";".join(structure) + "\n")
    elif qe_type == "378":
        with open("Export 378.csv", "a+") as csv:
            headers = [
                "ESPSEQ",
                "ENTCODIGO",
                "MRFMESANO",
                "QUAID",
                "TPMOID",
                "CMPID",
                "RAMCODIGO",
                "ESPDATAINICIORO",
                "ESPDATAFIMRO",
                "ESPDATAEMISSRO",
                "ESPVALORMOVRO",
                "ESPDATAINICIORD",
                "ESPDATAFIMRD",
                "ESPDATAEMISSRD",
                "ESPVALORMOVRD",
                "ESPCODCESS",
                "ESPFREQ",
                "ESPVALORCARO",
                "ESPVALORCARD",
                "ESPVALORCIRO",
                "ESPVALORCIRD",
                "ESPMOEDA"]
            csv.write(";".join(headers) + "\n")
            for arquivo in arquivos:
                with open(arquivo) as txt:
                    for linha in txt.readlines():
                        linha = linha.strip()
                        structure = [
                            linha[0:7],
                            linha[7:12],
                            linha[12:20],
                            linha[20:23],
                            linha[23:27],
                            linha[27:31],
                            linha[31:35],
                            linha[35:43],
                            linha[43:51],
                            linha[51:59],
                            linha[59:72],
                            linha[72:80],
                            linha[80:88],
                            linha[88:96],
                            linha[96:109],
                            linha[109:114],
                            linha[114:118],
                            linha[118:131],
                            linha[131:144],
                            linha[144:157],
                            linha[157:170],
                            linha[170:173]]
                        csv.write(";".join(structure) + "\n")
    elif qe_type == "404":
        with open("Export 404.csv", "a+") as csv:
            headers = [
                "MSASEQ",
                "ENTCODIGO",
                "MRFMESANO",
                "TPMORESSID",
                "GRACODIGO",
                "MSATIPOPERA",
                "MSANUMSIN",
                "MSANUMCONT",
                "MSATIPOCONT",
                "MSACODCESS",
                "MSADATACOMUNICA",
                "MSADATAREG",
                "MSADARAOCORR",
                "MSAVALORMOV",
                "MSATIPOSIN",
                "MSAMODCONT",
                "MSAMOEDA",
                "MSABASEIND",
                "MSAVALORMON"]
            csv.write(";".join(headers) + "\n")
            for arquivo in arquivos:
                with open(arquivo) as txt:
                    for linha in txt.readlines():
                        linha = linha.strip()
                        structure = [
                            linha[0:7],
                            linha[7:12],
                            linha[12:18],
                            linha[18:21],
                            linha[21:23],
                            linha[23:24],
                            linha[24:44],
                            linha[44:70],
                            linha[70:71],
                            linha[71:76],
                            linha[76:84],
                            linha[84:92],
                            linha[92:100],
                            linha[100:113],
                            linha[113:114],
                            linha[114:116],
                            linha[116:119],
                            linha[119:120],
                            linha[120:133]]
                        csv.write(";".join(structure) + "\n")
    elif qe_type == "405":
        with open("Export 405.csv", "a+") as csv:
            headers = [
                "MSASEQ",
                "ENTCODIGO",
                "MRFMESANO",
                "TPMORESSID",
                "GRACODIGO",
                "MSRNUMSIN",
                "MSRNUMCONT",
                "MSRTIPOCONT",
                "MSRCODCESS",
                "MSRDATACOMUNICA",
                "MSRDATAREG",
                "MSRVALOROCORR",
                "MSRVALORMOV",
                "MSRTIPOSIN",
                "MSRMODCONT",
                "MSRMOEDA",
                "MSRDASEIND",
                "MSRVALORMON"]
            csv.write(";".join(headers) + "\n")
            for arquivo in arquivos:
                with open(arquivo) as txt:
                    for linha in txt.readlines():
                        linha = linha.strip()
                        structure = [
                            linha[0:7],
                            linha[7:12],
                            linha[12:18],
                            linha[18:21],
                            linha[21:23],
                            linha[23:43],
                            linha[43:69],
                            linha[69:70],
                            linha[70:75],
                            linha[75:83],
                            linha[83:91],
                            linha[91:99],
                            linha[99:112],
                            linha[112:113],
                            linha[113:115],
                            linha[115:118],
                            linha[118:119],
                            linha[119:132]]
                        csv.write(";".join(structure) + "\n")
    elif qe_type == "406":
        with open("Export 406.csv", "a+") as csv:
            headers = [
                "SLASEQ",
                "ENTCODIGO",
                "MRFMESANO",
                "GRACODIGO",
                "SLATIPOPERA",
                "SLANUMSIN",
                "SLANUMCONT",
                "SLATIPOCONT",
                "SLACODCESS",
                "SLADATACOMUNICA",
                "SLADATAREG",
                "SLADATAOCORR",
                "SLAVALORMOVPEN",
                "SLAVALORMOVTOT",
                "SLATIPOSIN",
                "SLAMODCONT",
                "SLAMOEDA",
                "SLABASEIND"]
            csv.write(";".join(headers) + "\n")
            for arquivo in arquivos:
                with open(arquivo) as txt:
                    for linha in txt.readlines():
                        linha = linha.strip()
                        structure = [
                            linha[0:7],
                            linha[7:12],
                            linha[12:18],
                            linha[18:20],
                            linha[20:21],
                            linha[21:41],
                            linha[41:67],
                            linha[67:68],
                            linha[68:73],
                            linha[73:81],
                            linha[81:89],
                            linha[89:97],
                            linha[97:110],
                            linha[110:123],
                            linha[123:124],
                            linha[124:126],
                            linha[126:129],
                            linha[129:130]]
                        csv.write(";".join(structure) + "\n")
    elif qe_type == "407":
        with open("Export 407.csv", "a+") as csv:
            headers = [
                "SLRSEQ",
                "ENTCODIGO",
                "MRFMESANO",
                "GRACODIGO",
                "SLRNUMSIN",
                "SLRNUMCONT",
                "SLRTIPOCONT",
                "SLRCODCESS",
                "SLRDATACOMUNICA",
                "SLRDATAREG",
                "SLRDATAOCORR",
                "SLRVALORMOVPEN",
                "SLRVALORMOVTOT",
                "SLRTIPOSIN",
                "SLRMODCONT",
                "SLRMOEDA",
                "SLRBASEIND"]
            csv.write(";".join(headers) + "\n")
            for arquivo in arquivos:
                with open(arquivo) as txt:
                    for linha in txt.readlines():
                        linha = linha.strip()
                        structure = [
                            linha[0:7],
                            linha[7:12],
                            linha[12:18],
                            linha[18:20],
                            linha[20:40],
                            linha[40:66],
                            linha[66:67],
                            linha[67:72],
                            linha[72:80],
                            linha[80:88],
                            linha[88:96],
                            linha[96:109],
                            linha[109:122],
                            linha[122:123],
                            linha[123:125],
                            linha[125:128],
                            linha[128:129]]
                        csv.write(";".join(structure) + "\n")
    elif qe_type == "408":
        with open("Export 408.csv", "a+") as csv:
            headers = [
                "MPRSEQ",
                "MRFMESANO",
                "TPMORESSID",
                "GRACODIGO",
                "MPRNUMCONT",
                "MPRNUMENDOSSO",
                "MPRCODESS",
                "MPRTIPOCONT",
                "MPRMODCONT",
                "MPRDATACEITE",
                "MPRDATACONTR",
                "MPRDATAINICIO",
                "MPRDATAFIM",
                "MPRPERCRISCO",
                "MPRVALORMOV",
                "MPRVALORMOVCOMIS",
                "MPRCODCORRET",
                "MPRVALORMOVCORRET",
                "MPRVIGMED",
                "MPRBASEIND",
                "MPRMOEDA",
                "MPRTAXACONV",
                "MPRDATAEMISS "]
            csv.write(";".join(headers) + "\n")
            for arquivo in arquivos:
                with open(arquivo) as txt:
                    for linha in txt.readlines():
                        linha = linha.strip()
                        structure = [
                            linha[0:7],
                            linha[7:12],
                            linha[12:18],
                            linha[18:21],
                            linha[21:23],
                            linha[23:24],
                            linha[24:50],
                            linha[50:56],
                            linha[56:61],
                            linha[61:62],
                            linha[62:64],
                            linha[64:72],
                            linha[72:80],
                            linha[80:88],
                            linha[88:96],
                            linha[96:109],
                            linha[109:115],
                            linha[115:128],
                            linha[128:141],
                            linha[141:146],
                            linha[146:148],
                            linha[148:149],
                            linha[149:152],
                            linha[152:165],
                            linha[165:173]]
                        csv.write(";".join(structure) + "\n")
    elif qe_type == "409":
        with open("Export 409.csv", "a+") as csv:
            headers = [
                "EMFSEQ",
                "ENTCODIGO",
                "MRFMESANO",
                "QUAID",
                "ATVCODIGO",
                "TPFOPERADOR",
                "FTRCODIGO",
                "LCRCODIGO",
                "TCTCODIGO",
                "TPECODIGO",
                "EMFPRAZOFLUXO",
                "EMFVLREXPRISCO",
                "EMFCNPJFUNDO",
                "EMFCODISIN",
                "EMFCODCUSTODIA",
                "EMFMULTIPLOFATOR",
                "EMFTXCONTRATADO",
                "EMFTXMERCADO",
                "TPFOPERADORDERIVATIVO",
                "EMFVLRDERIVATIVO",
                "EMFCODGRUPO"]
            csv.write(";".join(headers) + "\n")
            for arquivo in arquivos:
                with open(arquivo) as txt:
                    for linha in txt.readlines():
                        linha = linha.strip()
                        structure = [
                            linha[0:7],
                            linha[7:12],
                            linha[12:18],
                            linha[18:21],
                            linha[21:23],
                            linha[23:49],
                            linha[49:55],
                            linha[55:60],
                            linha[60:61],
                            linha[61:63],
                            linha[63:71],
                            linha[71:79],
                            linha[79:87],
                            linha[87:95],
                            linha[95:101],
                            linha[101:114],
                            linha[114:127],
                            linha[127:132],
                            linha[132:145],
                            linha[145:147],
                            linha[147:148],
                            linha[148:151],
                            linha[151:164],
                            linha[164:172]]
                        csv.write(";".join(structure) + "\n")