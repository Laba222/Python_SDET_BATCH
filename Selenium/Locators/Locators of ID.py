import time
from selenium import webdriver
from selenium.webdriver.common.by import  By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("hello msg")
time.sleep(5)




