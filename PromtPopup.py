from time import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://nxtgenaiacademy.com/alertandpopup/")
driver.find_element(By.XPATH,"//button[@name ='promptalertbox1234']").click()
time.sleep(5)
alert = driver.switch_to.alert
time.sleep(5)
a = alert.text
print(a)
alert.accept()
driver.close()