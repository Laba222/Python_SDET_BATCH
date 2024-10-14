from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,"//input[starts-with(@class,'submit-button')]").click()
driver.close()