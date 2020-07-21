from selenium import webdriver
import unittest
class A(unittest.TestCase):
    def test_firstTest(self):
        print("test case 1")
        self.driver=webdriver.Chrome('C:\servers\chromedriver.exe')
        self.driver.get('https://support.google.com/mail/answer/56256?hl=en')
        print(self.driver.title)
        self.driver.close()
    def test2(self):
        print("test case 2")
        self.driver = webdriver.Chrome('C:\servers\chromedriver.exe')
        self.driver.get('https://www.facebook.com')
        print(self.driver.title)
        self.driver.close()


if __name__=="__main__":
    unittest.main()
