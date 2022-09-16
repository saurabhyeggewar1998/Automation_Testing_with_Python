import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.in/")
title = driver.execute_script("return document.title;")
print(title)

#To get alert notifications
driver.execute_script("alert('hello Saurabh');")