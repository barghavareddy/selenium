from selenium import webdriver
import logging
logging.basicConfig(filename="C:\errorsinlogging\logfille.log",format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
logging.debug("debuggin is done")
logging.info("info done")
logging.error("error is done")
logging.critical("critical condition")
logging.warning(" warning  ------")