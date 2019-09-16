# Actuarial Services By [Grant Thornton Brasil](https://www.grantthornton.com.br/en/service/advisory/actuarial-services/ "ActuarialServicesGrantThornton")

## What is this?

This is a tool that audit TXTs files sent to [SUSEP](http://www.susep.gov.br "SUSEP"), following their [manual](https://www2.susep.gov.br/download/fip2_2/Fip22_ManualPreenchimentosetembro-2019.zip "manual").
Unfortunately, this is very specific to the Brazilian insurance market, so the SUSEP's manual is entire in Portuguese :sleeping:

### How to use it
This tool was developed and tested in a Python 3.7 environment, so it's highly recommended to use the same version:
[Python 3](https://www.python.org/downloads/ "Python 3")

1.  install the requirements using pip
```
bs4
ciso8601
openpyxl
pandas
pycpfcnpj
requests
win10toast
```
2. Clone the project
3. Execute QEAuditor.pyw