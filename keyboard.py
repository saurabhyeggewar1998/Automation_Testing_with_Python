import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.select import Select

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.find_element(By.NAME,"email").send_keys("saurabh@gmail.com")
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.ENTER).perform()