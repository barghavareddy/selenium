from select import select

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('C:\servers\chromedriver.exe')
driver.get('https://www.swiggy.com')
d=driver.find_elements(By.TAG_NAME,"a")
print(len(d))
for link in d:
    print(link.text)

#driver.find_element_by_link_text("About us").click()
driver.find_element_by_partial_link_text("Abo").click()
