from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\servers\chromedriver.exe')
driver.get("https://www.facebook.com")
d = driver.find_elements(By.CSS_SELECTOR,"input[class='inputtext _58mg _5dba _2ph-']")
print(len(d))
