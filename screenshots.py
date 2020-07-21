from selenium import webdriver
driver=webdriver.Chrome('C:\servers\chromedriver.exe')
driver.get('https://www.facebook.com')
driver.maximize_window()
driver.save_screenshot("C:\screen___shots\homepa.png")

