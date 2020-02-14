# Actuarial Services By [Grant Thornton Brasil](https://www.grantthornton.com.br/en/service/advisory/actuarial-services/ "ActuarialServicesGrantThornton")
![](https://raw.githubusercontent.com/Grant-Thornton-Brasil/ActuarialServices/2aa7ee24fe7a81087c9854c0efb97e89ef188df3/Docs/demo.gif)
## What is this?

This is a tool that audits TXTs files sent to [SUSEP](http://www.susep.gov.br "SUSEP"), following their [manual](https://www2.susep.gov.br/download/fip2_2/Fip22_ManualPreenchimentosetembro-2019.zip "manual").
Unfortunately, this is very specific to the Brazilian insurance market, so the SUSEP's manual is entire in Portuguese :sleeping:

### How to use it
This tool was developed and tested in a Python 3.7 environment, so it's highly recommended to use the same version:
[Python 3](https://www.python.org/downloads/ "Python 3")

1. Install [Microsoft Visual C++ 14.2 standalone: Build Tools for Visual Studio 2019 (x86, x64, ARM, ARM64)](https://wiki.python.org/moin/WindowsCompilers#Microsoft_Visual_C.2B-.2B-_14.2_standalone:_Build_Tools_for_Visual_Studio_2019_.28x86.2C_x64.2C_ARM.2C_ARM64.29)
2.  install the requirements using pip
```
bs4
ciso8601
openpyxl
pandas
pycpfcnpj
pyodbc
requests
win10toast
```
```
pip install -U setuptools pip bs4 ciso8601 openpyxl pandas pycpfcnpj pyodbc requests win10toast --user
```
3. Install Microsoft Build Tools 2015
4. Clone the project
5. Execute \_\_main__.pyw
