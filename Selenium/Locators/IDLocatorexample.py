import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.nykaa.com/")
print(driver.find_element(By.ID,"category").text)
time.sleep(5)
driver.find_element(By.ID,"category").click()
time.sleep(5)
driver.close()
