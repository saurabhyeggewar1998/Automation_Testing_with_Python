from time import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
#driver.get("https://www.istqb.in/#")
driver.get("https://www.actimind.com/")
admin=driver.find_element(By.XPATH,"/html/body/header/div/div/div/nav/ul/li[2]/a" )
element=driver.find_element(By.XPATH,"/html/body/header/div/div/div/nav/ul/li[2]/ul/li/ul/li[1]/a")
action=ActionChains(driver)
action.move_to_element(admin).move_to_element(element).click().perform()



