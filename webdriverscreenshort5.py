from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.org/")
driver.save_screenshot("C:/Users\Dell/PycharmProjects/pythonProjectAutomationDemo/amazon.png")