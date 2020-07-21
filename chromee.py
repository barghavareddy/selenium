import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('C:\servers\chromedriver.exe')
driver.get('https://www.facebook.com')
print(driver.title)
print(driver.current_url)
#print(driver.page_source)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="email"]').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="email"]').send_keys(Keys.SHIFT,"BHARGAV")
time.sleep(2)
#driver.find_element_by_xpath("//*[@id='u_0_2']").click()




