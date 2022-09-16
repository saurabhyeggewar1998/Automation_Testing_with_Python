import time
from unittest import TestCase

import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
from Page.homepage import homepage
from Page.loginpage import LoginPage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        serv_obj = Service("F:/Selenium/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=serv_obj)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")

        login = LoginPage(driver)
        login.enter_username("7057114002")
        login.enter_passsward("29071998")
        login.click_login()

        home_page = homepage(driver)
        #home_page.click_on_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test successfully done")


if __name__=='__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="C:/Users/Dell/PycharmProjects/New folder/Report"))