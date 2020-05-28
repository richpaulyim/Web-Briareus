# Everything Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Other Modules
from bs4 import BeautifulSoup
import requests
from ScreenerPath import *
from LoginCredentials import *
import time                 

# INITIALIZE CHROME WEBDRIVER
x = webdriver.PhantomJS()
x.get(screen_login)

x.find_element_by_xpath("//input[@class='phone-no ' and @id='login-username']").send_keys(email)
# CLICK NEXT
x.find_element_by_xpath("//input[@id='login-signin']").submit()


# SEND PASSWORD KEYS
WebDriverWait(x, 5).until(EC.element_to_be_clickable(\
    (By.XPATH, '//*[@id="login-passwd"]'))).send_keys(password)
    
# FORCE WAIT UNTIL CERTAIN ELEMENTS ARE CLICKABLE
WebDriverWait(x, 30).until(EC.element_to_be_clickable(\
    (By.XPATH, '//*[@id="mbr-forgot-link"]')))
WebDriverWait(x, 30).until(EC.element_to_be_clickable(\
    (By.XPATH, '//*[@id="password-toggle-button"]'))) 
WebDriverWait(x, 30).until(EC.visibility_of_element_located(\
    (By.CLASS_NAME, 'challenge-button'))) 
    
# CLICK NEXT    
nextlink = x.find_element_by_class_name('challenge-button')
nextlink.click()

print("yes")