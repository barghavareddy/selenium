import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('C:\servers\chromedriver.exe')
driver.get('https://www.calculator.net/calorie-calculator.html')
driver.find_elements_by_css_selector("div[id='othercalc']>a")
d=driver.find_elements_by_tag_name("a")
print(len(d))

