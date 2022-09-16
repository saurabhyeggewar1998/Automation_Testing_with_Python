from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://omayo.blogspot.com/2013/05/page-one.html")
driver.find_element(By.ID,"uploadfile").send_keys("C:/Users\Dell/PycharmProjects/pythonProjectAutomationDemo/amazon.png")
