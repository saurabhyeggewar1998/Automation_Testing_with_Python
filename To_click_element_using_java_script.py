import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.in/")
best_sellers = driver.find_element(By.PARTIAL_LINK_TEXT,"Best Sellers")
driver.execute_script("arguments[0].click();",best_sellers)
time.sleep(5)
driver.close()