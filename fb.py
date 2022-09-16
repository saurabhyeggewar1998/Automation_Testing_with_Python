
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.select import Select

serv_obj = Service("F:/Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
#driver.find_element(By.NAME,"email").send_keys("saurabh")
#driver.find_element(By.ID,"pass").send_keys("12456")
driver.find_element(By.PARTIAL_LINK_TEXT,"Create New").click()
driver.find_element(By.NAME,"firstname").send_keys("saurabh")
driver.find_element(By.NAME,"lastname").send_keys("yeggewar")
driver.find_element(By.NAME,"reg_email__").send_keys("9325375293")
driver.find_element(By.NAME,"reg_passwd__").send_keys("886767")
#day=Select(driver.find_element(By.NAME,"day"))
#day.select_by_visible_text("29")
#month=Select(driver.find_element(By.NAME,"month"))
#month.select_by_visible_text("jul")
#month=Select(driver.find_element(By.NAME,"year"))
#month.select_by_visible_text("1998")
driver.find_element(By.NAME,"birthday_day").send_keys("29")
driver.find_element(By.NAME,"birthday_month").send_keys("july")
driver.find_element(By.NAME,"birthday_year").send_keys("1998")
driver.find_element(By.XPATH, "//label[text() = 'Male']").click()
driver.find_element(By.NAME,"websubmit").click()