

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
source_element=driver.find_element(By.XPATH,"//*[@id='box6']")
target_element=driver.find_element(By.XPATH,"//*[@id='box106']")
action=ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()
