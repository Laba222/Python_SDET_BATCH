import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# driver.get("https://www.google.com/")
# driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
lgn_btn=driver.find_element(By.NAME,"login-button")
time.sleep(4)
print(lgn_btn.text)
time.sleep(4)
print(lgn_btn.get_attribute('value'))
print(lgn_btn.get_attribute("type"))
driver.quit()
