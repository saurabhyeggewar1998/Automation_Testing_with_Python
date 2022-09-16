import os
import time
import unittest

import HTMLTestRunner
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        serv_obj = Service('F:/Selenium/chromedriver.exe')
        cls.driver = webdriver.Chrome(service=serv_obj)



    def test_search_bridgelabz(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME,"q").send_keys("Bridgelabz.com")
        time.sleep(3)
        self.driver.find_element(By.NAME,"btnK").click()

    def test_search_selenium(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME, "q").send_keys("Selenium with python")
        time.sleep(5)
        self.driver.find_element(By.NAME, "btnK").click()




    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        print("Test Completed....")

if __name__=='__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="C:/Users/Dell/PycharmProjects/New folder/\Report"))