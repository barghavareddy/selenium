from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Ie(r'C:\servers\IEDriverServer.exe')
driver.get('https://www.youtube.com')
print(driver.title)
driver.quit()