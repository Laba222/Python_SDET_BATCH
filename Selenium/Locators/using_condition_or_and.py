from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,"//input[@id='user-name' or @class='input_error form_input']").send_keys("welcome")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='password' and @class='input_error form_input']").send_keys("marry")
driver.close()