import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

print("1:chrome")
print("2:Explorer")
choice = int(input("Enter your choice"))
if choice == 1:
    serv_obj = Service("F:/Selenium/chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
if choice == 2:
    serv_obj1 = Service("F:/Selenium/chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj1)
driver.get("https://www.facebook.com/")
driver.forward()
driver.get("https://www.amazon.in/")
driver.forward()
time.sleep(4)
driver.close()