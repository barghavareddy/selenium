from select import select
from telnetlib import EC
from selenium.webdriver.support import expected_conditions
import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome('C:\servers\chromedriver.exe')
driver.get('https://www.swiggy.com')
driver.maximize_window()
# wait=WebDriverWait(driver,10)
# ele=wait.until(expected_conditions.element_to_be_clickable(driver.find_element_by_xpath("//*[@id='city-links']/div/ul[2]/li[112]/a").click()))
driver.find_element_by_xpath("//*[@id='city-links']/div/ul[2]/li[112]/a").click()
driver.back()
driver.find_element_by_partial_link_text("Team").click()
hand=driver.window_handles
for i in hand:
    driver.switch_to.window(i)
    print(driver.title)


print("exit-----------")