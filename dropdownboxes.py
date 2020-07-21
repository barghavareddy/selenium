from select import select

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('C:\servers\chromedriver.exe')
driver.get('https://support.google.com/mail/answer/56256?hl=en')

driver.find_element_by_css_selector("a[class='action-button']").click()
driver.implicitly_wait(10)
d=driver.find_elements(By.CSS_SELECTOR,"input[id='firstName']")
d.send_keys("bhargav")

#d.send_keys("bhargav")

# dr1=select(dr)
# #dr1.select_by_value()
# print(dr1.options)
# print(len(dr1.options))
