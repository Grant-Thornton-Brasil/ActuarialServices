import os
from glob import glob
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(os.path.join(here, "requirements.txt")) as reqs:
    requirements = reqs.read().split("\n")

setup(
    name="susepaudittool",
    version="0.0.1",
    description="Ferramenta feita em Python para auxiliar a auditoria de quadros estatísticos da SUSEP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcelo-franceschini/ActuarialServicesGrantThornton",
    author="Marcelo Majer Franceschini",
    author_email="marcelo.majer@yahoo.com.br",
    license="GPL-3.0",
    keywords="GUI SUSEP auditoria quadros estatísticos grant thornton seguros resseguros capitalização",
    # Shit must be fixed
    """
    packages=[
        "susepaudittool",
        "susepaudittool.susepaudittool.QEMaths",
        "susepaudittool.susepaudittool.QEMaths.Insurance",
        "susepaudittool.susepaudittool.QEMaths.Reinsurance",
        "susepaudittool.susepaudittool.QEMaths.Capitalization",
        "susepaudittool.susepaudittool.QEValidations.Insurance",
        "susepaudittool.susepaudittool.QEValidations.Reinsurance",
        "susepaudittool.susepaudittool.QEValidations.Capitalization",
    ],
    """
    python_requires=">=3.5",
    install_requires=requirements,
    # Shit must be fixed
    """
    data_files={"Excel Models\\Insurance":glob(os.path.join("Excel Models", "Insurance") + "\\*.xlsx"),
    "Excel Models\\Reinsurance": glob(os.path.join("Excel Models", "Reinsurance") + "\\*.xlsx"),
    "Excel Models\\Capitalization": glob(os.path.join("Excel Models", "Capitalization") + "\\*.xlsx")},
    """
    project_urls={
        "Grant Thornton": "https://www.grantthornton.com.br/servicos/consultoria/servicos-atuariais/",
        "SUSEP": "http://www.susep.gov.br/",
        "SUSEP FIP Manual": "http://www.susep.gov.br/menu/informacoes-ao-mercado/envio-de-dados-a-susep/fipsusep",
        "SUSEP FIP Manual up to date": "https://www2.susep.gov.br/download/fip2_2/Fip22_ManualPreenchimentosetembro-2019.zip",
    },
)