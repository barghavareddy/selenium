import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('C:\servers\chromedriver.exe')

driver.get('https://www.swiggy.com')
driver.maximize_window()
#driver.execute_script("window.scrol lBy(0,1000)","")
time.sleep(3)

# dr=driver.find_element_by_xpath("//*[@id='city-links']/div/ul[2]/li[112]/a")
# time.sleep(3)
# #driver.execute_script("arguments[0].scrollIntoView();",dr)
# time.sleep(3)
# dr.click()
# print("kk---- done----")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

