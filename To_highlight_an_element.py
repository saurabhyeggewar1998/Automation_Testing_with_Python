import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.in/")
highlight = driver.find_element(By.PARTIAL_LINK_TEXT,"Mobiles")
driver.execute_script("arguments[0].style.border = '3px solid red'",highlight)

#highlighting element using XPATH
highlight1 = driver.find_element(By.XPATH,"//div[@id = 'navSwmHoliday']")
driver.execute_script("arguments[0].style.border = '3px solid red'",highlight1)
time.sleep(5)
driver.close()