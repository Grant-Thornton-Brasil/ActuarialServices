from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium import webdriver
import os


class SES():

    def __init__(self):
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        path = os.path.abspath(
            os.path.join(
                os.path.abspath(__file__),
                "..",
                "chromedriver.exe"))
        self.driver = webdriver.Chrome(executable_path=path, options=options)

    def get_ramos(self, entcodigo, year):
        try:
            # Get
            self.driver.get(
                r"https://www2.susep.gov.br/menuestatistica/SES/premiosesinistros.aspx?id=54")
            # Find Data Elements
            datestart = self.driver.find_element_by_xpath(
                r'//*[@id="ctl00_ContentPlaceHolder1_edInicioPer"]')
            dateend = self.driver.find_element_by_xpath(
                r'//*[@id="ctl00_ContentPlaceHolder1_edFimPer"]')
            # Clear and Fill Data Elements
            datestart.clear()
            dateend.clear()
            datestart.send_keys(str(year) + "01")
            dateend.send_keys(str(year) + "12")
            # Find Selector and deselect all
            selector_element = self.driver.find_element_by_xpath(
                r'//*[@id="ctl00_ContentPlaceHolder1_edEmpresas"]')
            select = Select(selector_element)
            select.deselect_all()
            # Get options
            entcodigos = []
            for option in select.options[1:]:
                entcodigos.append(option.text[0:5])
            if entcodigo not in entcodigos:
                self.driver.quit()
                return False
            # In case it finds the entcodigo, select the "ramo"
            entcodigo = entcodigo.ljust(10, " ")
            select.select_by_value(entcodigo)
            # Select "Ramos Radio Button"
            self.driver.find_element_by_xpath(
                r'//*[@id="ctl00_ContentPlaceHolder1_optAgrupamento"]/tbody/tr[2]/td/label').click()
            # Click GO Process
            self.driver.find_element_by_xpath(
                r'//*[@id="ctl00_ContentPlaceHolder1_btnProcessao"]').click()
            # Wait for table to load
            try:
                table = WebDriverWait(
                    self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_gvSaida"]/tbody')))
            except BaseException:
                pass
            ramos = []
            for ramo in table.text.split("\n")[1:-1]:
                ramos.append(ramo[:4])
            self.driver.quit()
            return ramos

        except BaseException:
            return False
