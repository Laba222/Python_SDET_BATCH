import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.NAME,"login-button").click()
time.sleep(5)
driver.close()



# https://www.flipkart.com/


import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")

driver.maximize_window()
clicksearch=driver.find_element(By.NAME,"q")
clicksearch.send_keys("Android mobile")
clicksearch.send_keys(Keys.RETURN)
# or clicksearch.click()
time.sleep(5)
driver.close()
