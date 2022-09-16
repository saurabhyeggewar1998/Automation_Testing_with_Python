from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# get geeksforgeeks.org
driver.get("https://www.facebook.com/")

# get geeksforgeeks.org
driver.get("https://www.amazon.org/")

# one step forward in browser history
driver.forward()