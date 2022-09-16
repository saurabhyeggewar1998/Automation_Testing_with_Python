import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://events.hubspot.com/accounts/login/")
driver.find_element(By.CSS_SELECTOR,"input[id='id_login']").send_keys("saurabh@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[id='id_password']").send_keys("saur123")
driver.find_element(By.XPATH,"//button[text() = 'Log in']").click()
#driver.find_element(By.LINK_TEXT,"Create account").click()
#driver.find_element(By.LINK_TEXT,"Reset password").click()
