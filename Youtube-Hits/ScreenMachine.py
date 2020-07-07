# Everything Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Other Modules
from bs4 import BeautifulSoup
import requests
from ScreenerPath import *
from datetime import datetime
import time

class ScreenMachine():

    def __init__(self, headless = False):

        # SET WEBDRIVER OPTIONS
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080");
        options.add_argument("--start-maximized");
        if headless:
            options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # INITIALIZE CHROME WEBDRIVER
        self.driver = webdriver.Chrome(options=options, executable_path=r'/home/richpaulyim/bin/chromedriver')
        self.driver.get("https://finance.yahoo.com/screener/new")


    def build_screener(self, verbose = True, clear = True):

        # MAKE SURE DRIVER IS ON SCREENER PAGE
        self.__screener_page__()

        # CLEAR DEFAULTS OPTION
        if clear:

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(\
               (By.CLASS_NAME, 'removeFilter')))
            default_filters = self.driver.find_elements_by_class_name("removeFilter")

            while len(default_filters) > 0:
                default_filters[0].click()
                if len(default_filters) == 1:
                    break
                default_filters = self.driver.find_elements_by_class_name("removeFilter")

        if verbose:
            print("Screener is ready for filters.")

        return self


    def __filter_menu__(self):

        self.__screener_page__()

        self.driver.find_element_by_class_name("addFilter").click()
        dropdown = self.driver.find_element_by_xpath(afterClickHTML)

        # BEAUTIFUL SOUP DROPDOWN LIST PARSER
        html = dropdown.get_attribute('innerHTML')
        dropList = BeautifulSoup(html, 'lxml')
        filterList = dropList.find_all(class_=filters)

        # PRINT AVAILABLE CRITERIA
        print("Below are the available screeners.")
        for index, screener in enumerate(filterList):
            print(str(index+1) + '.', screener.get_text(),sep = " ")

        self.driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[3]/div/div/div[3]/button').click()


    def filter_config(self, val = 5, greater = True, verbose=True):

        """
        Select region, volume change and percentange change (intraday)
        """

        # open filter menu
        self.driver.find_element_by_class_name("addFilter").click()
        # find, click intraday
        intraday = self.driver.find_element_by_xpath(intra)
        intraday.click()
        # find, click exchange
        exchange = self.driver.find_element_by_xpath(exdelt)
        exchange.click()

        # close the menu
        self.driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[3]/div/div/div[3]/button').click()
        # select NASDAQ AND NYSE
        x = self.driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[2]/div/div[2]/ul/li/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div/ul/li[2]/label/span').click()
        self.driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div/ul/li[7]/label/span').click()
        time.sleep(2)

        # select percentage change bound
        if not greater:
            # select less than
            self.driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[1]/span[2]/div/span').click()
            time.sleep(2)
            self.driver.find_element_by_xpath(
                ".//*[contains(text(), 'less than')]"
            ).click()
            time.sleep(2)
        x = self.driver.find_element_by_xpath(
            '//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/input')
        x.click()
        x.send_keys(str(val))
        time.sleep(1.5)

        # Find stocks
        self.driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]/span/span').click()
        time.sleep(2)
        # show 100 rows
        try:
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[2]/span/div/span').click()
            self.driver.find_element_by_xpath(
            ".//*[contains(text(), 'Show 100 rows')]"
        ).click()
            time.sleep(2)
        except:
            # there may be less than 15 stocks under the filter
            pass

        # stock parsing
        group = requests.get(self.driver.current_url)
        groupdata = group.text
        groupsoup = BeautifulSoup(groupdata, "lxml")
        values = []
        for listing in groupsoup.find_all('tr', attrs={'class': 'simpTblRow'}):
            for value in listing.find_all('td'):
                values.append(value.text)
        values = [values[x:x + 8] for x in range(0, len(values), 10)]

        for i in range(0, len(values)):
            try:
                    values[i][1] = values[i][1][:17] + "..."
                    values[i][2] = float(values[i][2].replace(",",""))
                    values[i][3] = float(values[i][3].replace(",",""))
                    values[i][4] = float(values[i][4][:-1].replace(",",""))
                    values[i].append(datetime.today().strftime("%d-%m-%y"))
            except:
                pass

        # final result list
        result = []
        for i in range(0, len(values)):
            if values[i][7] != 'N/A':
               result.append(tuple(values[i]))
        if verbose:
            print(len(result))
            print(result)

        return(result)


    def parent_config(self):

        """
        Looking up United States, greater than 1
        """

        region = self.driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li/div/div')
        region.click()


    def done(self):

        self.driver.close()


    def __percentage_options__(self):

        self.__screener_page__()

        self.driver.find_element_by_class_name("addFilter").click()
        dropdown = self.driver.find_element_by_xpath(afterClickHTML)

        # BEAUTIFUL SOUP DROPDOWN LIST PARSER
        html = dropdown.get_attribute('innerHTML')
        dropList = BeautifulSoup(html, 'lxml')
        filterList = dropList.find_all(class_=filters)

        # PRINT AVAILABLE CRITERIA
        print("Below are screeners with percentages.")
        i = 1
        for index, screener in enumerate(filterList):
            if("%" not in screener.get_text()):
                continue
            else:
                print(str(i)+ '.', screener.get_text(),sep = " ")
            i = i + 1


        self.driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[3]/div/div/div[3]/button').click()


    def __screener_page__(self):

        if self.driver.current_url != "https://finance.yahoo.com/screener/new":

            self.driver.get("https://finance.yahoo.com/screener/new")
