from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('C:\servers\chromedriver.exe')
driver.get('https://www.facebook.com')
driver.implicitly_wait(5)

a=driver.find_element_by_name("email")
print(a.is_displayed())
print(a.is_enabled())
print(driver.title)
assert "Facebook – log in or sign up" in driver.title
driver.find_element_by_name("email").send_keys("95423069@gmail.com")
driver.find_element_by_id("pass").send_keys("78931255")
                                                             #c=driver.find_element_by_css_selector("input[id='u_0_b']")
                                                             #print(c.is_selected())
driver.find_element_by_id("u_0_b").click()
