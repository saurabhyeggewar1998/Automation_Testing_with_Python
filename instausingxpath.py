import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.select import Select

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.instagram.com/")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name ='username']").send_keys("saurabh")
driver.find_element(By.XPATH,"//input[@name = 'password']").send_keys("12345654")
#driver.find_element(By.XPATH,"//*[@type='submit']").click()
driver.find_element(By.XPATH,"//div[text() = 'Log In']").click()
#driver.find_element(By.XPATH,"//span[text() = 'Sign up']").click()
#time.sleep(1)
#for sign up process
#driver.find_element(By.XPATH,"//input[@name= 'emailOrPhone']").send_keys("8867747886")
#driver.find_element(By.XPATH,"//input[@name= 'fullName']").send_keys("saurabh g yeggewar")
#driver.find_element(By.XPATH,"//input[@name= 'username']").send_keys("saurabh")
#driver.find_element(By.XPATH,"//input[@name= 'password']").send_keys("saura1234")
#driver.find_element(By.XPATH,"//button[text() = 'Sign up']").click()