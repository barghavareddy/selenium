import unittest
from selenium import webdriver

class Abcd(unittest.TestCase):
    def test_sample(self):
        self.driver=webdriver.Chrome('C:\servers\chromedriver.exe')
        self.driver.get("http://www.google.com")
        titleof=self.driver.title
        self.assertFalse("Google1"==titleof,"noooo___")

if __name__=="__main__":
        unittest.main()
