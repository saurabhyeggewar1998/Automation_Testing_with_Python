from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.NAME,"proceed").click()
alt=driver.switch_to.alert
alt_text=alt.text
print("Alert text is ",alt_text)
alt.accept()
driver.find_element(By.NAME,"login").send_keys("Selinum")