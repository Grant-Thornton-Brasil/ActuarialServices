import os
import requests
from bs4 import BeautifulSoup
    
def get_ramos(entcodigo, ano, qe_type):
    ramos = []
    try:
        if qe_type in [376, 377, 378]:
            request = requests.get(
                "https://www2.susep.gov.br/menuestatistica/SES/premiosesinistros.aspx?id=54")
            sopa = BeautifulSoup(request.text, "html.parser")

            params = (('id', '54'))
            data = {
                '__VIEWSTATE': sopa.find("input", {"name": "__VIEWSTATE"})["value"],
                '__VIEWSTATEGENERATOR': sopa.find("input", {"name": "__VIEWSTATEGENERATOR"})["value"],
                '__EVENTVALIDATION': sopa.find("input", {"name": "__EVENTVALIDATION"})["value"],
                'ctl00$ContentPlaceHolder1$edEmpresas': entcodigo.ljust(10, " "),
                'ctl00$ContentPlaceHolder1$edInicioPer': str(ano)+"01",
                'ctl00$ContentPlaceHolder1$edFimPer': str(ano)+"12",
                'ctl00$ContentPlaceHolder1$optAgrupamento': 'RAM',
                'ctl00$ContentPlaceHolder1$btnProcessao': 'Processar'}

            request = requests.post(
                'https://www2.susep.gov.br/menuestatistica/SES/premiosesinistros.aspx', params=params, data=data)
            sopa = BeautifulSoup(request.text, "html.parser")
            elements = sopa.find_all("td", {"align": "left"})
            for element in elements[3:]:
                ramos.append(element.text[:4])
        elif qe_type in [404, 405, 406, 407, 408, 409]:
            request = requests.get(
                "https://www2.susep.gov.br/menuestatistica/SES/valoresresmovgrupos.aspx?tipo=premios&id=56")
            sopa = BeautifulSoup(request.text, "html.parser")
            request.cookies.get("ASP.NET_SessionId")

            cookies = {
                'ASP.NET_SessionId': request.cookies.get("ASP.NET_SessionId"),
                'ASPSESSIONIDSESRACTA': request.cookies.get("ASPSESSIONIDSESRACTA")}

            params = (('tipo', 'premios'), ('id', '56'))

            data = {
                '__VIEWSTATE': sopa.find("input", {"name": "__VIEWSTATE"})["value"],
                '__VIEWSTATEGENERATOR': sopa.find("input", {"name": "__VIEWSTATEGENERATOR"})["value"],
                '__EVENTVALIDATION': sopa.find("input", {"name": "__EVENTVALIDATION"})["value"],
                'ctl00$ContentPlaceHolder1$edEmpresas': entcodigo.ljust(10, " "),
                'ctl00$ContentPlaceHolder1$edInicioPer': str(ano)+"01",
                'ctl00$ContentPlaceHolder1$edFimPer': str(ano)+"12",
                'ctl00$ContentPlaceHolder1$optAgrupamento': 'GRU',
                'ctl00$ContentPlaceHolder1$btnProcessao': 'Processar'}

            request = requests.post(
                'https://www2.susep.gov.br/menuestatistica/SES/valoresresmovgrupos.aspx', params=params, cookies=cookies, data=data)
            sopa = BeautifulSoup(request.text, "html.parser")
            elements = sopa.find_all("td", {"align": "left"})
            for element in elements[3:]:
                ramos.append(element.text[:2])
        return ramos
    except:
        return False
        
def get_esrcodcess():
    html = requests.get("https://www2.susep.gov.br/menuestatistica/SES/valoresresmovgrupos.aspx?tipo=sinistros&id=57").text
    sopa= BeautifulSoup(html, "html.parser")
    esrcodcess = []
    table = sopa.find("select", {"name":"ctl00$ContentPlaceHolder1$edEmpresas"})
    for element in table.find_all("option")[1:]:
        esrcodcess.append(element.text[:5].strip())
    return esrcodcess
