import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Autoit:
    def uplodfile(self):

        serv_obj = Service("F:/Selenium/chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get("https://ps.uci.edu/~franklin/doc/file_upload.html")
        #time.sleep(3)
        driver.find_element(By.XPATH,"//input[@name='userfile']").click()
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        release_file = (r"F:\Selenium\filedemo.exe")
        os.system(release_file)
        #time.sleep(10)
        #driver.close()

Auto = Autoit()
Auto.uplodfile()