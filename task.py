from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.find_element(By.CSS_SELECTOR,"input[id='email']").send_keys("saurabh@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[id='pass']").send_keys("saur123")
driver.find_element(By.PARTIAL_LINK_TEXT,"Create New").click()
#driver.find_element(By.CSS_SELECTOR,"input[id='u_2_b_IM']").send_keys("saurabh")
