from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.select import Select

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.find_element(By.NAME,"email").send_keys("veeresh")
driver.find_element(By.ID,"pass").send_keys("12456")
driver.find_element(By.PARTIAL_LINK_TEXT,"Create New").click()
#time.sleep(2)
driver.find_element(By.NAME,"firstname").send_keys("rohit")
driver.find_element(By.NAME,"lastname").send_keys("sharama")
driver.find_element(By.NAME,"reg_email__").send_keys("8867743684")
driver.find_element(By.NAME,"reg_passwd__").send_keys("8867743")
driver.find_element(By.NAME,"birthday_day").send_keys("10")
driver.find_element(By.NAME,"birthday_month").send_keys("jan")
driver.find_element(By.NAME,"birthday_year").send_keys("1998")
driver.find_element(By.XPATH, "//label[text() = 'Male']").click()
driver.find_element(By.NAME,"websubmit").click()