import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.select import Select

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://connect.starthotspot.com/SignIn")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("saurabh@gmail.com")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Rabbu123")
driver.find_element(By.XPATH,"//*[@type='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='btnSignUp']").click()
