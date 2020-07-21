import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('C:\servers\chromedriver.exe')
driver.get('https://www.facebook.com')
print(driver.title)
print(driver.current_url)
time.sleep(20)
driver.get('https://www.youtube.com')
print(driver.title)
print(driver.current_url)
time.sleep(20)
driver.back()
print(driver.title)
print(driver.current_url)
driver.forward()
print(driver.title)
print(driver.current_url)



time.sleep(20)
#driver.find_element_by_xpath('//*[@id="u_0_2"]').click()

driver.close()